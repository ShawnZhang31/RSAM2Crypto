//
//  ViewController.m
//  RSAM2CryptoDemo
//
//  Created by 张晓民 on 2019/8/10.
//  Copyright © 2019 张晓民. All rights reserved.
//

#import "ViewController.h"
#import <RSAM2Crypto/RSAM2.h>

#define PASSWORD @"123456"
#define ENC_BY_PUB_PYTHON @"GDmYI0mM+VmLqnKNz/0+3IK1bQ53krBarUm5LUbOA0CEDKX46XhsECSXlCUyzcgf7FcEXP5mHWjwaK1vmkJME/dVdfMedtC7DVGStDtiWvbgn6HJssMMcA2hfBeAGZ9PFeLf3hElHQ4oEoIyLsnfd3ErQ++DeAd8W9JfBiCcBq5piMJe4JhR08oY//PjxuHYeJMbctVVO2yZtivKp8pnIquxzdrOQyZvPH/c1Qsr9uVEDMFhZOKUcK21nSN/gSZViwXj3jlEcBLG+ebFrhKnP4VMDy5xMvmQ2DvtNz11ivBiGtmpX80mjAMIHOcOcdUTbuoPjHO+RiB9JSkUiaQZXA=="
#define ENC_BY_PRI_PYTHON @"KA7eXR2NVaCzWVyxGRY7p2HlYwPFtccy1qFq+ZklJ3iZ1EPi4netrgdHfdonTgOJhyLj62/4AJ0t7dhJv8aJGNGGO7eD3rlTjojd+D/BmBnXNV3Jg3o94+Xre27QjHb9wx9NvRVnjp+0WrSMBlmgNoqGadMEhL+EV5ke9BDBdQ8qA2o37mIPLquG47b1qc0EbrsL38oGcSv33GM6aptIoF1BPQzCrYCcs0ILyZ1sMpZR/RMvDI3GMbdDmDpU4DiarmrRM2Dv469de95CWKgMjfvVgKhU+8tYVIM0YAsNaSA/KJ0S9FQQ29kCuQ8Na132CKEhcSNuTbydKuEmvYH7AA=="


@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
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
    
    
//    NSLog(@"private_p12_path:%@",private_p12_path);
//    NSLog(@"public_der_path:%@",public_der_path);
//    NSLog(@"private_pem_contents:%@",private_pem_contents);
//    NSLog(@"public_pem_contents:%@",public_pem_contents);
    
    
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


@end
