# 加密
k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
def enctry(s):
    encry_str = ""
    for i,j in zip(s,k):
        # i为字符，j为秘钥字符
        temp = str(ord(i)+ord(j))+'_' # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
        encry_str = encry_str + temp
    return encry_str

# 解密
def dectry(p):
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):
        # i 为加密字符，j为秘钥字符
        temp = chr(int(i) - ord(j))
        dec_str = dec_str+temp
    return dec_str
