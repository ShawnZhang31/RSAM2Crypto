import M2Crypto
import base64
import os

prefix=os.path.dirname(os.path.abspath(__file__))

# 公钥路径
public_key_filename = os.path.join(prefix, '../cers/public_key.pem')
# 私钥路径
private_key_filename = os.path.join(prefix, '../cers/private_key.pem')

#使用公钥加密
def public_encrypt(data,public_key,padding=M2Crypto.RSA.pkcs1_padding):
    '''使用公钥对字符串进行加密
        这里演示的如何加密字符串，如果需要加密字符串以外的内容，可以将要加密的数据转换为bytes，然后使用公钥的public_encrypt方法直接加密
    Args:
        data, 需要加密的字符串；
        public_key, 公钥文件的路径；
        padding, 加密的padding方式，默认是pkcs1
    return:
        返回Base64编码的字符串
    '''
    data_encode = data.encode()
    ras_pri = M2Crypto.RSA.load_pub_key(public_key)
    ctrx_pri = ras_pri.public_encrypt(data_encode, padding)
    ctrx64_pri = (base64.b64encode(ctrx_pri)).decode('utf-8')
    return ctrx64_pri

#使用私钥解密
def private_decrypt(msg,private_key,padding=M2Crypto.RSA.pkcs1_padding):
    '''使用私钥对字符串进行解密
        这里演示的如何加密字符串，如果需要解密字符串以外的内容，可以将要解密的数据转换为bytes，然后使用私钥直接解密
    Args:
        msg, Base64编码的加密字符串；
        private_key, 私钥文件的路径；
        padding, 加密的padding方式，默认是pkcs1
    return:
        返回UTF-8编码的字符串
    '''
    msg_encode = msg.encode('utf-8')
    msg_bytes = base64.b64decode(msg)
    ras_pri = M2Crypto.RSA.load_key(private_key)
    output = ras_pri.private_decrypt(msg_bytes, padding)
    return output.decode('utf-8')

#使用私钥加密
def private_encrypt(data, private_key, padding=M2Crypto.RSA.pkcs1_padding):
    '''使用私钥对字符串进行加密
        这里演示的如何加密字符串，如果需要加密字符串以外的内容，可以将要加密的数据转换为bytes，然后使用私钥直接加密
    Args:
        data, 需要加密的字符串；
        private_key, 私钥文件的路径；
        padding, 加密的padding方式，默认是pkcs1
    return:
        返回Base64编码的字符串
    '''
    data_encode = data.encode()
    ras_pri = M2Crypto.RSA.load_key(private_key)
    ctrx_pri = ras_pri.private_encrypt(data_encode, padding)
    ctrx64_pri = (base64.b64encode(ctrx_pri)).decode('utf-8')
    return ctrx64_pri

#使用公钥解密
def public_decrypt(msg,public_key,padding=M2Crypto.RSA.pkcs1_padding):
    '''使用公钥对字符串进行解密
        这里演示的如何解密字符串，如果需要解密字符串以外的内容，可以将要解密的数据转换为bytes，然后使用私钥直接解密
    Args:
        msg, Base64编码的加密字符串；
        public_key, 公钥文件的路径；
        padding, 加密的padding方式，默认是pkcs1
    return:
        返回UTF-8编码的字符串
    '''
    msg_encode = msg.encode('utf-8')
    msg_bytes = base64.b64decode(msg_encode)
    ras_pri = M2Crypto.RSA.load_pub_key(public_key)
    output = ras_pri.public_decrypt(msg_bytes, padding)
    return output.decode('utf-8')

data='这是一个测试，this is a test!'

print('原始数据:%s'%data)
message_public_encrypted = public_encrypt(data, public_key_filename)
print("公钥加密数据:%s"%message_public_encrypted)
message_private_decrypted= private_decrypt(message_public_encrypted, private_key_filename)
print("私钥解密公钥加密数据:%s"%message_private_decrypted)
message_private_encrypted = private_encrypt(data, private_key_filename)
print("私钥加密数据:%s"%message_private_encrypted)
message_public_decrypted= public_decrypt(message_private_encrypted, public_key_filename)
print("公钥解密私钥加密数据:%s"%message_public_decrypted)

