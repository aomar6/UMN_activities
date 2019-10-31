# Signing Documents

In this activity, you'll use GPG to
- Sign documents
- Verify signatures
- Generate clearsigned documents and detached signatures

## Instructions

Create a new directory for this assignment, or simply save your work in `~/tmp`.

### Signing and Verifying Documents

- Store a small message in a file called `document`.
  - **Solution**: `echo "small message, huh?" >> document`

- Use GPG to sign and encrypt the document.
  - **Solution**: `gpg --output document.sig --sign document`

- Trade signed documents with your seat partner, and verify/decrypt each other's documents.
  - **Solution**: `gpg --output document.partner --decrypt partners_document.sig`

- Next, open your signed document in a text editor. It'll contain binary data, and be unintelligible, but you can still edit it. 

- Delete a random character, and trade the document with your seat partner again. What happens when you try to verify/decrypt?
  - **Solution**: GPG won't decrypt the document. This is because editing the file invalidated the signature.

### Clearsigned Documents

- Repeat the above exercise, but generate a clearsigned document instead of an encrypted one.
  - **Solution**: `gpg --output document.sig --clearsign document`

- Inspect the clearsigned document. What's the difference? How would you verify the signature?
  - **Solution**: The clearsigned document contains the unencrypted original message, with the PGP signature attached at the end. You'd have to edit the file to extract and verify the signature.
  - **Note**: PGP stands for Pretty Good Privacy, and is a program that GPG uses to provide encryption.

### Verifying Detached Signatures

- Repeat the above exercise, but generate a detached signature.
  - **Solution**: `gpg --output document.sig --detach-sig document`

## Questions

- What are the advantages to generating a detached signature? What are the disadvantages?
  - **Solution**: The advantage is that the encrypted message contains _only_ the relevant data, instead of the data and the signature. This is also a disadvantage, in that both pieces must be transmitted separately to preserve both privacy and authenticity. Which method is appropriate depends on whether you need both privacy and authenticity, or primarily privacy.

