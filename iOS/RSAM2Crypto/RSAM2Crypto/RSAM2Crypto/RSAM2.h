//
//  RSAEncryptor.h
//  RSA
//
//  Created by 张晓民 on 2019/8/8.
//  Copyright © 2019 张晓民. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <Security/Security.h>
NS_ASSUME_NONNULL_BEGIN

@interface RSAM2 : NSObject

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

///**
// * 使用.der格式的公钥验证私钥签名数据
// *  注意验证私钥签名数据时需要出入的algorithm参数与私钥签名时传入的参数必须一样
// *
// * @param origin 需要验证的原始数据
// * @param signature 私钥签名后的Base64编码的字符串
// * @param path .der格式的公钥文件的路径
// * @param algorithm 私钥签名的算法
// *
// * @return 如果验证成功则返回YES，验证不成功则返回NO
// */
//
//+ (BOOL)verifyString:(NSString *)origin andSignature:(NSString *)signature publicKeyWithContentsOfFile:(NSString *)path withAlgo:(SecKeyAlgorithm)algorithm;

///**
// * 使用.p12格式的私钥对字符串进行签名
// *  使用私钥签名的字符串必须使用公钥进行签名验证
// *
// * @param str 需要签名的字符串
// * @param path .p12格式的私钥的路径
// * @param password 私钥的密码，如果私钥没有设置密码请传入 @""
// * @param algorithm 签名算法，注意不是所有的签名算法都是可以使用的，在设置算法钱请确认算法可用
//
// * @return 返回base64n编码的签名字符串
// */
//+ (NSString *)signString:(NSString *)str privateWithContentsOfFile:(NSString *)path password:(NSString *)password withAlgo:(SecKeyAlgorithm)algorithm;



///**
// * 使用.p12格式的私钥对字符串进行签名
// *  使用私钥签名的字符串必须使用公钥进行签名验证
// *
// * @param str 需要签名的字符串
// * @param path .p12格式的私钥的路径
// * @param password 私钥的密码，如果私钥没有设置密码请传入 @""
// * @return 返回base64编码的签名字符串
// */
//+ (NSString *)signString:(NSString *)str privateWithContentsOfFile:(NSString *)path password:(NSString *)password;

///**
// * 使用.der格式的公钥对字符串进行签名
// *  使用公钥签名的字符串必须使用私钥进行签名验证
// *
// * @param str 需要签名的字符串
// * @param path .der格式的公钥的路径
// *
// * @return 返回base64编码的签名字符串
// */
//+ (NSString *)signString:(NSString *)str publicWithContentsOfFile:(NSString *)path;

///**
// * 使用.pem格式的私钥对字符串进行签名
// *  使用私钥签名的字符串必须使用公钥进行签名验证
// *
// * @param str 需要签名的字符串
// * @param keyContens 使用.pem格式的私钥对字符串进行签名
// * @param isPrivate 是否是私钥
// * @return 返回base64编码的签名字符串
// */
//+ (NSString *)signString:(NSString *)str pemKeyContents:(NSString *)keyContens isPrivate:(BOOL)isPrivate;

///**
// * 使用.der格式的公钥验证私钥签名数据
// *
// * @param origin 需要验证的原始数据
// * @param signature 私钥签名后的Base64编码的字符串
// * @param path .der格式的公钥文件的路径
// *
// * @return 如果验证成功则返回YES，验证不成功则返回NO
// */
//
//+ (BOOL)verifyString:(NSString *)origin andSignature:(NSString *)signature publicKeyWithContentsOfFile:(NSString *)path;

///**
// * 使用.p12格式的私钥验证公钥签名数据
// *
// * @param origin 需要验证的原始数据
// * @param signature 公钥签名后的Base64编码的字符串
// * @param path .p12格式的私钥文件的路径
// * @param password 私钥的密码，如果私钥没有设置密码请传入 @""
// *
// * @return 如果验证成功则返回YES，验证不成功则返回NO
// */
//
//+ (BOOL)verifyString:(NSString *)origin andSignature:(NSString *)signature privateKeyWithContentsOfFile:(NSString *)path password:(NSString *)password;

///**
// * 使用.pem格式的秘钥验证秘钥签名数据
// *    使用公钥签名的字符串必须使用私钥进行签名验证，使用私钥签名的字符串必须使用公钥进行签名验证
// * @param origin 需要验证的原始数据
// * @param signature 公钥签名后的Base64编码的字符串
// * @param keyContens pem格式的秘钥文件中的字符
// * @param isPrivate 是否是私钥
// *
// * @return 如果验证成功则返回YES，验证不成功则返回NO
// */
//
//+ (BOOL)verifyString:(NSString *)origin andSignature:(NSString *)signature pemKeyContents:(NSString *)keyContens isPrivate:(BOOL)isPrivate;

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



@end

NS_ASSUME_NONNULL_END
