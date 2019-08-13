# RSAM2Crypto
在iOS中实现RSA加密、解密，支持Python的M2Crypto、Java、PHP。  
在进行项目开发的使用Python(Flask)开发的后台需要使用RSA与Android和iOS客户的进行数据加密与解密。由于各种秘钥格式有所不同，加密的时候的使用的补位算法也不同，所以Web后台与iOS和Android的加密与解密就出现的一些小问题。   
iOS一般是使用p12格式的私钥的，iOS的RSA加密与解密主要是使用Security.framework提供的实现完成的。不过iOS官方给出的加密方案只能公钥加密私钥解密，私钥不能用于加密，私钥只能签名，使用公钥验证签名。而在在某些应用场景下也是需要使用私钥加密公钥解密。为此对Security.framwork的RSA的实现进行了重新封装并实现了:  
**iOS公钥加密私钥解密，私钥加密公钥解密，同时支持der公钥、p12私钥、pkcs1和pkcs5格式的pem密钥，该方案生成的证书只是python、java和php的调用**

- [1.工程目录](#1工程目录)  
- [2.安装](#2安装)  
    - [2.1 RSAM2Crypto.framework的配置](#21-rsam2cryptoframework的配置)       
    - [2.2 RSAM2Crypto.framework的方法说明](#22-rsam2cryptoframework的方法说明)
    - [2.3 RSAM2Crypt.framework使用实例](#23-rsam2cryptframework使用实例) 
- [3. 证书的生成](#3-证书的生成)
    - [3.1 生成证书的脚本解释](#31-生成证书的脚本解释) 
    - [3.2 秘钥加密的字符串长度限制](#32-秘钥加密的字符串长度限制)
- [更新说明](#更新说明)  


## 1.工程目录
```
cers/
    -Android_private_key.pem------------------供Android使用的私钥
    -Android_public_key.pem-------------------供Android使用的公钥
    -iOS_private_key.p12----------------------iOS使用的p12格式的私钥
    -iOS_public_key.der-----------------------iOS使用的der格式的公钥
    -iOS_private_key.pem----------------------iOS使用的pem格式的私钥
    -iOS_public_key.pem-----------------------iOS使用的pem格式的公钥
    -private_key.pem--------------------------python、php、java使用的私钥
    -public_key.pem---------------------------python、php、java使用的公钥
iOS/
    RSAM2Crypto/
                RSAM2Crypto/------------------RSAM2Crypto.framework的源码工程
                RSAM2CryptoDemo/--------------RSAM2Crypto.framework调用演示工程
               -RSAM2Crypto.xcworkspace-------RSAM2Crypto xcode workplace
Python/
    -certs_test.py----------------------------python调用示例工程，使用pipenv管理
```
## 2.安装
### 2.1 RSAM2Crypto.framework的配置
在release中下载发布的[RSAM2Crypto.framework.zip](https://github.com/ShawnZhang31/RSAM2Crypto/releases/download/v1.2/RSAM2Crypto.framework.zip),解压获取RSAM2Crypto,.framework,或者clone工程在自行编译RSAM2Crypto.framework。在工程的Link Binary With Libraries中添加RSAM2Crypto.framework和Security.framwork即可。
### 2.2 RSAM2Crypto.framework的方法说明
在需要使用的RSAM2Crypto.framework的地方插入:
```Objective-C
#import <RSAM2Crypto/RSAM2.h>
```
RSAM2.h定义的主要方法是:
```Objective-C
/**
 * 使用.der格式的公钥对字符字符串进行加密
 *  使用使用公钥加密的内容必须使用私钥进行解密
 * @param str 需要加密的字符串
 * @param path .der格式的公钥文件的路径
 *
 * @return 返回base64编码的加密字符串
 */
+ (NSString *)encryptString:(NSString *)str publicKeyWithContentsOfFile:(NSString *)path;

/**
 * 使用PKCS1格式的公钥字符串内容进行加密
 *  使用使用公钥加密的内容必须使用私钥进行解密
 * @param str 需要加密的字符串
 * @param pub_str 公钥的字符串内容
 *
 * @return 返回base64编码的加密字符串
 */
+ (NSString *)encryptString:(NSString *)str publicKeyString:(NSString *)pub_str;

/**
 * 使用.p12格式的私钥对字符字符串进行加密
 *  使用使用私钥加密的内容必须使用公钥进行解密
 * @param str 需要加密的字符串
 * @param path .p12格式的公钥文件的路径
 * @param password 私钥的密码，如果私钥没有设置密码请传入 @""
 *
 * @return 返回base64编码的加密字符串
 */
+ (NSString *)encryptString:(NSString *)str privateWithContentsOfFile:(NSString *)path password:(NSString *)password;

/**
 * 使用PKCS8格式的私钥字符串内容进行加密
 *  使用使用私钥加密的内容必须使用公钥进行解密
 * @param str 需要加密的字符串
 * @param pri_str 私钥的字符串内容
 *
 * @return 返回Base64编码的加密字符串
 */
+ (NSString *)encryptString:(NSString *)str privateKeyString:(NSString *)pri_str;

/**
 * 使用PKCS1格式的公钥字符串对私钥加密的数据进行解密
 *
 * @param str 私钥加密后的Base64编码格式的字符串
 * @param pub_str PKCS1格式的公钥字符串
 *
 * @return 公钥解密后的UTF-8编码的字符串
 */
+ (NSString *)decryptString:(NSString *)str publicKeyString:(NSString *)pub_str;

/**
 * 使用.der格式的公钥文件对私钥加密的数据进行解密
 *
 * @param str 私钥加密后的Base64编码格式的字符串
 * @param path .der格式的公钥文件的路径
 *
 * @return 公钥解密后的UTF-8编码的字符串
 */
+ (NSString *)decryptString:(NSString *)str publicKeyWithContentsOfFile:(NSString *)path;

/**
 * 使用.p12格式的私钥文件对公钥加密的数据进行解密
 *
 * @param str 公钥加密后的Base64编码格式的字符串
 * @param path .p12格式的公钥文件的路径
 * @param password 私钥的密码，如果私钥没有设置密码请传入 @""
 *
 * @return 私钥解密后的UTF-8编码的字符串
 */
+ (NSString *)decryptString:(NSString *)str privateKeyWithContentsOfFile:(NSString *)path password:(NSString *)password;

/**
 * 使用PKCS8格式的私钥字符串对公钥加密的数据进行解密
 *
 * @param str 私钥加密后的Base64编码格式的字符串
 * @param pri_str PKCS8格式的私钥字符串
 *
 * @return 私钥解密后的UTF-8编码的字符串
 */
+ (NSString *)decryptString:(NSString *)str privateKeyString:(NSString *)pri_str;
```
### 2.3 RSAM2Crypt.framework使用实例
RSAM2方法调用示例:
```Objective-C
{
    // 证书路径
    NSString *private_p12_path = [[NSBundle mainBundle] pathForResource:@"iOS_private_key.p12" ofType:nil];
    NSString *public_der_path = [[NSBundle mainBundle] pathForResource:@"iOS_public_key.der" ofType:nil];
    NSString *private_pem_path = [[NSBundle mainBundle] pathForResource:@"iOS_private_key.pem" ofType:nil];
    NSString *public_pem_path = [[NSBundle mainBundle] pathForResource:@"iOS_public_key.pem" ofType:nil];
    
    // pem证书的内容
    NSString *private_pem_contents = [self readContetsFromPemFile:private_pem_path];
    NSString *public_pem_contents = [self readContetsFromPemFile:public_pem_path];
    
    // 加密前的明文
    NSString *originStr = @"这是一个测试，this is a test!";
    
    
    // 使用der公钥加密的密文
    NSString *enc_by_der_pub = [RSAM2 encryptString:originStr publicKeyWithContentsOfFile:public_der_path];
    NSLog(@"使用der公钥加密的密文:\n%@", enc_by_der_pub);
    // 使用pem公钥加密的密文
    NSString *enc_by_pem_pub = [RSAM2 encryptString:originStr publicKeyString:public_pem_contents];
    NSLog(@"使用pem公钥加密的密文:\n%@", enc_by_pem_pub);
    // 使用.p12私钥加密的密文
    NSString *enc_by_p12_pri = [RSAM2 encryptString:originStr privateWithContentsOfFile:private_p12_path password:PASSWORD];
    NSLog(@"使用.p12私钥加密的密文:\n%@", enc_by_p12_pri);
    // 使用pem秘钥加密的密文
    NSString *enc_by_pem_pri = [RSAM2 encryptString:originStr privateKeyString:private_pem_contents];
    NSLog(@"使用pem私钥加密的密文:\n%@", enc_by_pem_pri);
    

    // 使用p12私钥解密der公钥加密的密文
    NSString *den_pub_der_using_pri_p12 = [RSAM2 decryptString:enc_by_der_pub privateKeyWithContentsOfFile:private_p12_path password:PASSWORD];
    NSLog(@"使用p12私钥解密der公钥加密的密文:\n%@",den_pub_der_using_pri_p12);
    // 使用p12私钥解密pem公钥加密的密文
    NSString *den_pub_pem_using_pri_p12 = [RSAM2 decryptString:enc_by_pem_pub privateKeyWithContentsOfFile:private_p12_path password:PASSWORD];
    NSLog(@"使用p12私钥解密pem公钥加密的密文:\n%@",den_pub_pem_using_pri_p12);
    // 使用p12私钥解密python pem公钥加密的密文
    NSString *den_python_pub_pem_using_pri_p12 = [RSAM2 decryptString:ENC_BY_PUB_PYTHON privateKeyWithContentsOfFile:private_p12_path password:PASSWORD];
    NSLog(@"使用p12私钥解密python pem公钥加密的密文:\n%@",den_python_pub_pem_using_pri_p12);
    
    // 使用pem私钥解密der公钥加密的密文
    NSString *den_pub_der_using_pri_pem = [RSAM2 decryptString:enc_by_der_pub privateKeyString:private_pem_contents];
    NSLog(@"使用pem私钥解密der公钥加密的密文:\n%@", den_pub_der_using_pri_pem);
    // 使用pem私钥解密pem公钥加密的密文
    NSString *den_pub_pem_using_pri_pem = [RSAM2 decryptString:enc_by_pem_pub privateKeyString:private_pem_contents];
    NSLog(@"使用pem私钥解密pem公钥加密的密文:\n%@", den_pub_pem_using_pri_pem);
    // 使用pem私钥解密python pem公钥加密的密文
    NSString *den_python_pub_pem_using_pri_pem = [RSAM2 decryptString:ENC_BY_PUB_PYTHON privateKeyString:private_pem_contents];
    NSLog(@"使用pem私钥解密python pem公钥加密的密文:\n%@", den_python_pub_pem_using_pri_pem);    
}

/**
 * 从pem文件中读取文件内容
 *
 * @param path 文件路径
 *
 * @return 返回UTF-8编码格式的字符
 */
- (NSString *) readContetsFromPemFile:(NSString *)path
{
    NSFileManager *fm = [NSFileManager defaultManager];
    NSData *data = [[NSData alloc] init];
    data = [fm contentsAtPath:path];
    return [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
}
```
## 3. 证书的生成
使用certs目录下的certs_g.sh shell脚本可以生成供iOS使用的：p12格式的私钥、der格式的公钥、pem格式的公钥以及pem格式的私钥；供Android使用的：pem格式的公钥、pem格式的私钥；供Web后台（Python、PHP、Java）使用的：pem格式的私钥和公钥。  
certs_g.sh的使用方法为:
```shell
# 为certs_g.sh脚本授权
chmod +x certs_g.sh 
# 运行脚本
./certs_g.sh
```
### 3.1 生成证书的脚本解释
```shell
# 生成给Python M2Crypto使用的PKCS1格式的2048位私钥
# 其他的私钥和公钥都是从该私钥派生出的
openssl genrsa -out private_key.pem 2048

# 生成Python M2Crypto使用的公钥public_key.pem
openssl rsa -in private_key.pem -out public_key.pem -pubout

# 生成证书请求文件rsaCertReq.csr
# 注意：这一步会提示输入国家、省份、mail等信息，可以根据实际情况填写，或者全部不用填写，直接全部敲回车.
openssl req -new -key private_key.pem -out rsaCerReq.csr


# 生成证书rsaCert.crt，并设置有效时间为10年，3650代表3650天
openssl x509 -req -days 3650 -in rsaCerReq.csr -signkey private_key.pem -out rsaCert.crt

# 生成供iOS使用的公钥文件iOS_public_key.der
openssl x509 -outform der -in rsaCert.crt -out iOS_public_key.der

# 生成供iOS使用的私钥文件iOS_private_key.p12
# 注意：这一步会提示给私钥文件设置密码，直接输入想要设置密码即可，然后敲回车，然后再验证刚才设置的密码，再次输入密码，然后敲回车，完毕！
openssl pkcs12 -export -out iOS_private_key.p12 -inkey private_key.pem -in rsaCert.crt

# 生成供iOS使用的pem格式的公钥iOS_public_key.pem
openssl rsa -in private_key.pem -out iOS_public_key.pem -pubout

# 生成供iOS使用的pem格式的私钥iOS_private_key.pem
openssl pkcs8 -topk8 -in private_key.pem -out iOS_private_key.pem -nocrypt

# 生成供Android使用的公钥Android_public_key.pem
openssl rsa -in private_key.pem -out Android_public_key.pem -pubout

# 生成供Android使用的私钥Android_private_key.pem
openssl pkcs8 -topk8 -in private_key.pem -out Android_private_key.pem -nocrypt

# 删除中间文件
rm -rf rsaCerReq.csr
rm -rf rsaCert.crt
# 所有平台的证书生成完毕
```
### 3.2 秘钥加密的字符串长度限制
RSA加密的可加密的数据长度与创建的私钥的大小有关。例如上面的秘钥生成方法中:  
```shell
openssl genrsa -out private_key.pem 2048
```
该方法生个的私钥大小为2048字节，一个字符位8个字节，所以理论上讲加密的字符串的字符个数不能超过2048÷8=256个字符，不过RSAM2Crypto.framework在加密的中使用了PKCS1的补位算法，PKCS1占用了11个字符，所以要加密的字符长度不能超过256-11=245个字符。**如果超过了请将长字符分段加密，再拼接在一起。**

## 更新说明
- 2019-08-14
    - RSAM2Crypto.framework v1.2版本
    - 修改的版本问题
    - 优化了加密效率
- 2019-08-13
    - RSAM2Crypto.framework v1.1版本
    - 支持公钥加密字符串、私钥解密；私钥加密，公钥解密；
    - 支持iOS、Android、Python、Java、PHP


