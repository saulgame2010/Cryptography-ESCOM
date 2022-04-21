# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

class Cipher:

	"""Regresa un objeto tipo RSA_KEY para poder operar con el texto"""
	@staticmethod
	def load_public_key(path):
		return RSA.import_key(open(path).read())

	"""Regresa un objeto tipo RSA_KEY para poder operar con el texto"""
	@staticmethod
	def load_private_key(path):
		return RSA.import_key(open(path).read())

	"""Genera la llave públic y privada para el usuario.
	IMPORTANTE: Guardar bien las llaves porque siempre genera diferentes"""
	@staticmethod
	def generate_keys():
		key = RSA.generate(2048)
		private_key = key.export_key()
		file_out = open("private_key.rsa", "wb")
		file_out.write(private_key)
		file_out.close()
		public_key = key.publickey().export_key()
		file_out = open("public_key.rsa", "wb")
		file_out.write(public_key)
		file_out.close()
	
	"""RECIBE:
		text - Son los bytes del texto a cifrar.
		public_key - Un objeto tipo RSA_KEY que corresponde a la clave pública
		file_output - Nombre (con extensión) del archivo de salida
	   IMPORTANTE: Llamar previamente a load_public_key(path)"""
	@staticmethod
	def encrypt(text,public_key,file_output):
		file_out = open(file_output, "wb")
		#recipient_key = RSA.import_key(open("receiver.pem").read())
		session_key = get_random_bytes(16)
		# Encrypt the session key with the public RSA key
		cipher_rsa = PKCS1_OAEP.new(public_key)
		enc_session_key = cipher_rsa.encrypt(session_key)
		# Encrypt the data with the AES session key
		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		encrypted_text, tag = cipher_aes.encrypt_and_digest(text)
		[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, encrypted_text) ]
		file_out.close()

	"""RECIBE:
		text - Son los bytes del texto a descifrar.
		private_key - Un objeto tipo RSA_KEY que corresponde a la clave privada
		file_output - Nombre (con extensión) del archivo de salida
	   IMPORTANTE: Llamar previamente a load_private_key(path)"""
	@staticmethod
	def decrypt(encrypted_file,private_key,file_output):
		file_out = open(file_output,"w");
		enc_session_key, nonce, tag, ciphertext = \
		[ encrypted_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
		# Decrypt the session key with the private RSA key
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		# Decrypt the data with the AES session key
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)
		file_out.write(data.decode("utf-8"))
		file_out.close()


	"""RECIBE: Bytes a firmar (message), llave privada y nombre del archivo de salida"""
	@staticmethod 
	def generate_signature(message,private_key,name):
		hash_obj = SHA1.new()
		hash_obj.update(message)
		signature = pkcs1_15.new(private_key).sign(hash_obj)		
		fou = open(name,"wb")
		fou.write(signature)
		fou.write(message)
		fou.close()

	@staticmethod
	def verify_signature(message,public_key):
		signature = message[256:]
		hash_obj = SHA1.new(signature)
		original_message = message[:256]
		try:
			pkcs1_15.new(public_key).verify(hash_obj,original_message)
			return 1
		except (ValueError, TypeError):
			return 0