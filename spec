17 03 03 20 40
97 5e c7
cc 2d a2 17 08 14 c1 20 
cd 18 e4 6a 1f 9d 

17 03 03 20 40 
b0 29 de 
9b 83 29 69 36 d6 77 e4
9b 02 ea 45 42 e1 


17 03 03  HEADER
11 50 	  LENGTH + 10
98 5b 26 
b5 d7 cc ea 
ec 15 7f a5 fc a5 d0 84 e9 13





log "AES Key Header: " {8:[rdx+.0]} " " {4:[rdx+.8]} "\nAES Key data: " {8:[rdx+c]} " " {8:[rdx+c+.8]} " " {8:[rdx+c+.16]} " " {8:[rdx+c+.24]}


dump2 keys:

bulk in 8:6A56DB3E80F6DC0B 8:74D6B42A391F3E05 8:F51A60DA31DBC8C7 8:BE40D4A499F13C68
bulk out 8:6D86E5353980468A 8:42E61E27944D492C 8:982A3131AB9A4B40 8:D6943971B5DA0FEE