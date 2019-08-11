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

# 使用der公钥加密的密文
msg_enc_pub_der="NjwFefNqadWSzEsVYsC0Rkoc+mc3g+Zlmt7LueMP9cTst5GONWAwGbqU081F1VOlWHr6B/O1G36TxPq1fq3iOFy3zUR1msRmlO9UakyuxH1Oa12vqT7txudqSTOdWoXqrDhhApa3VpVAfTJ9kmVkZZ0GLvJkjse1gBUBR7kBcNDq2R3d1wnnkYC0bqXFPS5ae2MKWhK4mqe0yNYy0TSJtaP3FyV3Oqt4he/5Its125wYjz7mk5WAenAmC2B3jN5guilb/3XpcgqVZEq6imCOVPcZB33c1/f3If0sv0PmjMLmOTm9pqfi9j1g0ZFz7tkmiylDylU1jjoconIvdisJXg=="
# 使用pem公钥加密的密文
msg_enc_pub_pem="mWl3l4NAHwwcp7vBnRLL7FbXSs7JShHDxXVz1nBDnTODtTcfUEYeV2+nDEVWf5TD4BOEbZ9CJwAUPofN6gUbinz1EcptFvNyta5iziB1HleqgIv23MpsSBs3lRhSlydhUMBKoRtnZzXPZGDKZXCMbXRJhZLYUwIctODcs8LiTDlHrhQVdmayVMELW2QESHQ5neQUVEYrr0TdmCuznvyC1FxfI4KVP5qw7MOJUk5CQCtt5XipC2B+FcWteg8koE7LjgPeO8o2uUImQig9lQ434UfWv2Yyc5pgvC4gzXpdrDmMCr9CdhJbutUdSvnm5ePu3YMRcRdbDyocZ0nmVx+zvQ=="
# 使用.p12私钥加密的密文
msg_enc_pri_p12="KA7eXR2NVaCzWVyxGRY7p2HlYwPFtccy1qFq+ZklJ3iZ1EPi4netrgdHfdonTgOJhyLj62/4AJ0t7dhJv8aJGNGGO7eD3rlTjojd+D/BmBnXNV3Jg3o94+Xre27QjHb9wx9NvRVnjp+0WrSMBlmgNoqGadMEhL+EV5ke9BDBdQ8qA2o37mIPLquG47b1qc0EbrsL38oGcSv33GM6aptIoF1BPQzCrYCcs0ILyZ1sMpZR/RMvDI3GMbdDmDpU4DiarmrRM2Dv469de95CWKgMjfvVgKhU+8tYVIM0YAsNaSA/KJ0S9FQQ29kCuQ8Na132CKEhcSNuTbydKuEmvYH7AA=="
# 使用pem私钥加密的密文
msg_enc_pri_pem="KA7eXR2NVaCzWVyxGRY7p2HlYwPFtccy1qFq+ZklJ3iZ1EPi4netrgdHfdonTgOJhyLj62/4AJ0t7dhJv8aJGNGGO7eD3rlTjojd+D/BmBnXNV3Jg3o94+Xre27QjHb9wx9NvRVnjp+0WrSMBlmgNoqGadMEhL+EV5ke9BDBdQ8qA2o37mIPLquG47b1qc0EbrsL38oGcSv33GM6aptIoF1BPQzCrYCcs0ILyZ1sMpZR/RMvDI3GMbdDmDpU4DiarmrRM2Dv469de95CWKgMjfvVgKhU+8tYVIM0YAsNaSA/KJ0S9FQQ29kCuQ8Na132CKEhcSNuTbydKuEmvYH7AA=="

print("私钥解密der公钥加密数据:%s"%private_decrypt(msg_enc_pub_der, private_key_filename))
print("私钥解密pem公钥加密数据:%s"%private_decrypt(msg_enc_pub_pem, private_key_filename))
print("公钥解密p12私钥加密数据:%s"%public_decrypt(msg_enc_pri_p12, public_key_filename))
print("公钥解密pem私钥加密数据:%s"%public_decrypt(msg_enc_pri_pem, public_key_filename))
