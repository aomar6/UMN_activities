# The Day DES Died

NIST used a competition model to land on a the standard that became AES. But such competitions are also used to determine which standards we should phase out.

RSA Security leveraged a similar model in their DES Challenges, in which cryptanalysts the world over applied themselves to uncover weaknesses in the Data Encryption Standard (DES), the precursor to AES. 

This exercise is your opportunity to learn more about it.

## Instructions

- Open the PDF provided in [Resources](./Resources), called **The Day DES Died**.

- Read the following sections:

  - Introduction

  - The RSA Challenge

  - The 2nd and 3rd Challenges

  - How Strong is Encryption?

  - Conclusion

    - Also read the paragraph immediately above Conclusion.

## Questions

- What are the minimum acceptable key lengths and cipher strengths nowadays?
  - **Solution**: Keys should be 1,048 bits long at minimum, and ciphers should operate on blocks of at least 128 bits in size.

- What was the purpose of RSA Challenge 1?
  - **Solution**: The purpose of RSA Challenge 1 was to see if crytographers could find out how to efficiently break DES encryption.

- What was the result of RSA Challenge 1?
  - **Solution**: RSA Challenge 1 ended with a programmer cracking DES encryption in 90 days. 

- How long did it take for contestants to crack the first of the two challenge messages in RSA Challenge 2? How long did it take to crack the second message?
  - **Solution**: It took 41 days to crack the first message. it took 56 hours to crack the second!

- What are the two most important factors determining the strength of an encryption algorithm?
  - **Solution**: The two most ipmortnat factors determining the strength of an encryption algorithm are the **effective length of its key** and **its ability to resist cryptanalysis**.

- How did cryptographers solve the problem of DES being easily breakable?
  - **Solution**: An immediate solution was the development of Triple DES, which essentially applies DES three times to strengthen its security guarantees.

- What does the story of DES reveal about ciphers that rely on fixed-length key sizes? 
  - **Solution**: Ciphers that rely on fixed-length key sizes will always be susceptible to brute-force attacks.
