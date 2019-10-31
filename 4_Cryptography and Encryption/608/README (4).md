# Orientation

In this activity, you'll familiarize yourself with some key terms in cryptography.

We'll cover each of these topics in-depth throughout the week. This exercise is simply meant to get you up to speed with the jargon before layering on depth.

## Instructions

### Goals of Cryptography

Use the resources provided to define, and provide an examples for, each of the following terms.

- **Privacy**: Ensuring that data is intelligible only to the intended audience.
  - **Example**: Encrypting a message containing information on military operations so eavesdroppers can't read the content.

- **Authenticity**: Ensuring that a message really was sent by the person who claims to have sent it.
  - **Example**: Including the general's signature on the aforementioned military ops document.

- **Integrity**: Ensuring that a message hasn't been tampered with during transit.
  - **Example**: Using a wax seal to close an envelope so it's obvious if someone opens the letter before it arrives at its destination.

- **Non-Repudiation**: Ensuring that a message can be irrefutably linked to its sender.
  - **Example**: Forcing parties to provide signatures on a contract to prove they were both present for its signing.

### Key Terms

- **Plaintext**: The "raw", readable text of a message.
  - **Example**: `"Troops: Attack at dawn!"`

- **Ciphertext**: The encrypted (transformed, "gibberish") version of a message.
  - **Example**: `"asf87: -?*(1@^sz!jjx..."`, an encrypted version of the above plaintxt message.

- **Code**: Any method for concealing the contents of a message.
  - **Example**: Cartels often use slang terms to refer to contraband they're shipping, e.g.: "The grass is in the trunk," where "grass" might be a code word.

- **Bit**: A "slot" that can be either a 0 or a 1.
  - **Example**: The binary number `1010` contains four bits.

- **Byte**: A collection of eight bits.
  - **Example**: The binary number `10100101` s a single byte, nad contains eight bits.

- **Cryptography**: The art and science of writing effective codes.

- **Cipher**: A set of rules for transforming a plaintext into a ciphertext, and back again.
  - **Example**: Pig Latin is a simple (and useless) cipher. It turns the plaintext "This is a message" into "Histay Isay Ay Essagemay" by moving the first consonant of each word to the end, and adding `-ay` after that.

- **Encryption**: The process of applying a cipher to a plaintext to generate an encrypted message.
  - **Example**: Generating "Histay Isay Ay Essagemay" using the Pig Latin transformation rules is an example of encryption.

- **Decryption**: The process of applying a cipher in reverse to recover plaintext from a given ciphertext.

- **Encryption Key**: A special value used to turn a plaintext into a ciphertext.
  - **Example**: We can turn the phrase "Hello" into "Ifmmp" by turning "H" into "I"; "e" into "f"; etc. In other words, we replace each letter with the next letter in the alphabet. In this case, the "key" is 1—we turn each letter of the plaintext into a letter of the ciphertext by replacing it with the letter _one_ space ahead in the alphabet.

- **Symmetric-Key Cryptography**: A method for encryption that uses the same key for encryption and decryption.
  - **Example**: Turning "Hello" into "Ifmmp" is an example of symmetric key cryptography.

- **Asymmetric-Key Cryptography**: A method for encryption that uses _different_ keys for encryption and decryption.
  - **Example**: No example was necessary for this definition, as we'll study it later. The takeaway is that symmetric methods aren't the _only_ methods.

- **Hash Signature**: A "fingerprint" of a file. In other words: A short value generated from a file, that is unique to the file.
  - **Example**: The hash signature of "Hello there" is: `e8ea7a8d1e93e8764a84a0f3df4644de`. The hash signature of "Hello there!" is: `a77b55332699835c035957df17630d28`. Even though the messages are similar, their hash signatures/"fingerprints" are completely different.
