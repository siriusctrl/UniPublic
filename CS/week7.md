### Transport layer security(TLS)

- Secure communication objects
  - **Private** communication
  - **Integrity checks** of data
  - **Authentication** of end point(s)
  
- SSL(secure socket layer)
  - Basis of HTTPS
  - Provides confidence the server is who it says it is (not others that try to pretend it is)
  - Encrypts transmission
    - Prevent eavesdropping and modification
  
- Choices of payload
  - TLS runs over TCP, which TLS payload type is TCP.
    - It did a little bit of <u>presentation layer</u> and <u>session layer</u> (OSI model) stuff.
    - Presentation layer
      - Encryption, data formatting and decryption
    - Session layer
      - Authentication
        - Provides confidence the server is who it says it is
      - Restoration of interrupted session
        - You close your laptop when downloading, if you open your laptop later, it don't need to download from the very beginning.
  - HTTPS uses port 443 instead of 80
    - Only way to identify what being sent is TLS
  - TLS is not a transport layer protocol, it is blow HTTP (might belongs to application layer)
  
- Handshake procedure

  - Establish TCP connection
  - Client sends 
    - ClientHello to server asking for secure connection
    - listing its supported “cipher suites”
  - Server responds
    - ServerHello
    - One of the cipher suites
    - Certificate
    - Request the client send its certificate
  - Client
    - Validate the certificate
  - Client generates
    - Session key
      1. It could pick a random key and encrypt it with public key of the server
      2. Run Diffie-Hellman
  - Handshake concludes and both parties share a key that is then used for encrypting/decrypting messages

  

### Cryptography

- Definitions
  - Encryption
    - Hide data and generate a cipher text based on some method. (Like RSA, factorising the product of 2 large primes)
  - Decryption
    - Recovering the original data from the cipher text using the key
  - Premise: secret key that is unknown to eavesdropper.
- Type
  - Symmetric Cryptography
    - Same key is used for encryption and decryption
    - Need to find some way to securely exchanging the secret key.
    - Useful for keeping your own data secure
      - Full disk encrypt
    - Modern example: AES (Advanced Encryption Standard)
      - AES breaks data into blocks and encrypts each block
      - Different modes of operation
        - ECB, CBC, CTR, etc.
        - Determines how each block is treated and/or linked.
  - Asymmetric Cryptography
    - Two keys, encrypt with one and decrypt with the other



### Symmetric cryptography method

- ECB (Electronic Codebook)
  - Simple use the key to encrypt each block
  - It is simple, parallelisable
  - Does not provide diffusion
    - when one block has been changed, the other block should also be changed as well
    - Same plaintext encrypts to the same cipher text (no diffusion)
      - ![image-20190422165301599](assets/image-20190422165301599.png)
    - Reprtition of patterns will be evident, though the pattern itself is not.
  - may not even provide confidentiality.
    - Where make sure that nobody in between site A and B is able to read what data or information is sent between the to sites.
  - Generally should never be used.
- CBC (Cipher Block chaining)
  - Primarily use an initialization vector to encode the plain text. For the following text, simply using the previous cipher text to encode.
    - Simlar as add salt to each encryption, so that the pattern won't be easily found.
  - Encryption must b e done sequentially
  - Decryption can be done in parallel since we only need previous cipher text.
  - Loss of a block or corrupt initial vector prevents decryption of next block.
  - Changing in any of the block will results in failing to decryption of the following blocks. (**Diffusion**)



### Asymmetric Cryptography (public key crypto)

- Two keys,  encrypt with one, decrypt with the other
- Everyone else can encrypt a message using the public key and send it to you. 
- Only you can use the private key to decrypt the message.
- <u>Compare</u> with symmetric cryptography
  - Asymmetric is slower
  - It often isn't suitable for encrypting large amounts of data
  - <u>Often used together</u> with symmetric cryptography as a way of exchanging a joint secret key
- Problem
  - Since normally the key last for a very long time (years), the attacker might have chance to get the private key.



### Diffie-Hellman key exchange

- Properties
  - It is symmetric way to generate secret key at both end
  - Provide forward secrecy
    - Even if long-term key (private key in the key pair) was compromised, and an attacker had recorded all traffic, they would still not be able to decrypt the messages.
  - Limit to conventional compromise
    - Can be break by a quantum computer
  - It allows both parties to calculate a shared key without having to ever explicitly communicate the shared key.
- Process
  1. Gemerate some public information
     1. A large prime p
     2. A generator g (primitive root modulo p)
  2. Alice picks a random value $a$ and computes $A=g^a \mod p$ 
     - Sends $A$ to Bob
  3. Bob picks a random value b and computes $B = g^b$ mod p
     - Send $B$ to Alice
  4. Alice calculates the secret $s=B^a \mod p \equiv g^{ba} \mod p$
  5. Bob calculates the secret $s=A^b \mod p \equiv g^{ab} \mod p$
- Why we need this?
  - We use this way to generate symmetric key at both end so that we could use symmetric cryptography to encrypt the content



### Cipher Suite

- Using a combination of cryptography method that works well together
- It including 
  1. Encoding/decoding algorithm
  2. Key exchange mechanism
  3. Parameters (key size)
- example
  - TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (0x0033)



### Public key signatures (usage of asymmetric cryptography)

- The inverse of encryption and decryption

- Provide non-repudiation

  - Cannot deny having signed the document

- Encrypt a message with the privateKey, anyone else can decrypt with the public key and verify that the message was signed by the private key holder.

- For large documents

  - Use a cryptographic hash function
    - e.g. SHA256
    - Takes a near arbitrary length input and fixed length outputs

  - Why hash?
    - Easy and fast to calculate
    - Infeasible to reverse
    - Extremely unlikely two slightly different documents produce the same hash

### Salt

- Non-secret randomness added to the plaintext
- Why we need this?
  - If someone use the same password at all sites, one sit is hacked $\to$ all sites compromised
- Store salt and SHA256 of (salt, password)
- Different has value at each sit now
- Easiest way is to append the salt at the back of the password



### Certificates

- Digitally signed documents that provide proof of identity or ownership
- The signer is a Certificate Authority (CA) pre-trusted by your browser/OS
  - Their work is to verify whether the website are who they said they are
- But not perfect
  - Create own local certificate authority and install certificate into root stores
  - Local proxy can intercept TLS connections
    - Not robust to man in the middle attack
  - Common practice for anti-virus/web protection software