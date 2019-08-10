#/*
# * @Author: Shawn Zhang 
# * @Date: 2019-08-10 14:32:20 
# * @Last Modified by:   Shawn Zhang 
# * @Last Modified time: 2019-08-10 14:32:20 
# */

echo "---start:生成给Python M2Crypto使用的PKCS1格式的2048位私钥..."
openssl genrsa -out private_key.pem 2048
echo "生成给Python M2Crypto格式的PKCS1格式的2048位私钥---end"

echo "---start:生成Python M2Crypto使用的公钥public_key.pem..."
openssl rsa -in private_key.pem -out public_key.pem -pubout
echo "生成Python M2Crypto使用的公钥public_key.pem---end"

echo "---start:生成证书请求文件rsaCertReq.csr..."
echo "注意：这一步会提示输入国家、省份、mail等信息，可以根据实际情况填写，或者全部不用填写，直接全部敲回车."
openssl req -new -key private_key.pem -out rsaCerReq.csr
echo "生成证书请求文件rsaCertReq.csr---end"


echo "---start:生成证书rsaCert.crt，并设置有效时间为10年..."
openssl x509 -req -days 3650 -in rsaCerReq.csr -signkey private_key.pem -out rsaCert.crt
echo "生成证书rsaCert.crt，并设置有效时间为10年---end"

echo "---start:生成供iOS使用的公钥文件iOS_public_key.der..."
openssl x509 -outform der -in rsaCert.crt -out iOS_public_key.der
echo "生成供iOS使用的公钥文件iOS_public_key.der---end"

echo "---start:生成供iOS使用的私钥文件iOS_private_key.p12..."
echo "注意：这一步会提示给私钥文件设置密码，直接输入想要设置密码即可，然后敲回车，然后再验证刚才设置的密码，再次输入密码，然后敲回车，完毕！"
openssl pkcs12 -export -out iOS_private_key.p12 -inkey private_key.pem -in rsaCert.crt
echo "生成供iOS使用的公钥文件iOS_public_key.der---end"

echo "---start:生成供iOS使用的pem格式的公钥iOS_public_key.pem..."
openssl rsa -in private_key.pem -out iOS_public_key.pem -pubout
echo "生成供iOS使用的pem格式的公钥iOS_public_key.pem---end"

echo "---start:生成供iOS使用的pem格式的私钥iOS_private_key.pem..."
openssl pkcs8 -topk8 -in private_key.pem -out iOS_private_key.pem -nocrypt
echo "生成供iOS使用的pem格式的私钥iOS_private_key.pem---end"


echo "---start:生成供Android使用的公钥Android_public_key.pem..."
openssl rsa -in private_key.pem -out Android_public_key.pem -pubout
echo "生成供Android使用的公钥Android_public_key.pem---end"

echo "---start:生成供Android使用的私钥Android_private_key.pem..."
openssl pkcs8 -topk8 -in private_key.pem -out Android_private_key.pem -nocrypt
echo "生成供Android使用的公钥Android_private_key.pem---end"

echo "清楚中间文件..."
rm -rf rsaCerReq.csr
rm -rf rsaCert.crt
echo "所有平台的证书生成完毕"