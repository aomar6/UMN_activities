# Encrypting with GPG

In this activity, you'll use GNU Privacy Guard (GPG) to
- Generate a public/private keypair
- Generate a revocation certificate
- Encrypt and decrypt data

## Instructions

Create a new directory called `~/.gpg_keys/my_key` to store your work in. Be sure to move into it before beginning the exercise.

### Generating Keypairs

- Use GPG to generate an RSA keypair.
  - **Solution**: `gpg --gen-key`, and select `4`.

- Inspect your public keyring.
  - **Solution**: `gpg --list-keys`

- Generate a revocation certificate. Store it in a file called `revoke.asc`.
  - **Solution**: `gpg --output revoke.asc --gen-revoke my_key`

- Export your public key with ASCII armor. Save it in a file called `your_name.gpg`, where `your_name` is, of course, your name.
  - **Solution**: `gpg --armor --output peleke.gpg --recipient ann@example.org urgent_memo`

- Send the `gpg` file to your seat partner in Slack.

- Upon receiving your partner's key, import it in your public keyring.
  - **Solution**: `gpg --import partner.gpg`

### Encryption/Decryption

- Create a file called `SecretFormula.YourName`, and write a top-secret message, which should include a number (any number will do).
  - **Solution**: `echo "I'm 42 years old." >> SecretFormula.Peleke`

- Encrypt the message with your partner's public key.
  - **Solution**: `gpg --output SecretFormula.Peleke.enc --recipient ann@example.org SecretFormula.Peleke`

- Send the encrypted message to your partner.

- Upon receiving your partner's encrypted message, decrypt it, and verify that the number you decrypted is the number they included in the original message.
  - **Solution**: `gpg --output SecretFormula.Peleke --decrypt SecretFormula.Peleke.enc`

#### Signing Documents

To encrypt and sign a document:

```
gpg --output signed_document.sig --sign input_file
```

To verify a signature and decrypt:

```
gpg --output unencrypted_output --decrypt signed_document.sig
```

If the signature is invalid, GPG will fail silently—i.e., it won't create `unencrypted_output`, but won't print an error message.

#### Clearsigned Documents

A **clearsigned document** is one containing an unencrypted message with an appended PGP signature.

To generate a clearsigned document:

```
gpg --output document.sig --clearsign document
```

#### Detached Signatures

To generate a detached signature:

```
gpg --output document.sig --detach-sig document
```

To verify a document with a detached signature:

```
gpg --verify document.sig document
```

## Questions

- What is a revocation certificate?
  - **Solution**: A revocation certificate is a document that invalidates a public key. In other words, it notifies the world that you no longer use the private key associated with the invalidated public key, so no one can use it to encrypt documents in the future.
