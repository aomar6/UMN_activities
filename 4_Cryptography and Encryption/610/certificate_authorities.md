# Certificate Authorities and Trust

## Questions

Relying on mutual trust in Certificate Authorities makes intuitive sense, but it has its disadvantages.

- What if someone you're trying to communicate with doesn't trust the CA that's verified your identity?
  - **Solution**: That's it: They don't trust it. This means they'll reject your certificate, and implies that _everyone_ must trust _someone_ for certificate authorities to work. Many consider this a critical shortcoming of CAs. 

- Imagine Eve tricks a CA into issuing her a certificate that says she's actually **Apple, Inc**.
  - How can Eve take advantage of this?
    - **Solution**: This allows Eve to forge her identity.
  - How would clients find out about such a mix-up?
    - **Solution**: They probably wouldn't—since Eve has a valid certificate stating that she's Apple, and everyone else trusts that certificate, they'll be none the wiser.
  - How would the CA Eve duped go about fixing this mistake?
    - **Solution**: The CA would have to revoke the certificate.

- Relying on certificate authorities isn't the _only_ way to establish trust in someone's identity. Read the **Simplified Explanation** of the Web of Trust: <https://en.wikipedia.org/wiki/Web_of_trust#Operation_of_a_web_of_trust>

  - How does the Web of Trust "prove" that a message came from a given individual? In other words: How does the Web of Trust use public/private keys to establish identity?
  - **Solution**: The Web of Trust establishes identity with digital signatures.

  - How is this different from the way Certificate Authorities establish identity?
  - **Solution**: The major difference is that this model does _not_ require everyone to trust a single, central authority.

  - In your own words, summarize one advantage and disadvantage of the CA model, and one advantage and disadvantage of the Web of Trust model.
  - **Solution**: The advantage is that the Web of Trust doesn't involve a "single source of truth". The disadvantage is that users must trust each _other_.

## Extension

- Read about the Verisign CA compromise at this link: <https://web.archive.org/web/20111026052552/http://support.microsoft.com/kb/293818>

- PGP is an encryption program that relies on the web of trust, and is used to encrypt a variety of data, including emails, files, and hard drives. 

- If you'd like to be extra safe and send _only_ encrypted email with your classmates, sign up for ProtonMail, a free email service that automatically encrypts emails you send to other ProtonMail users: <https://protonmail.com/>
