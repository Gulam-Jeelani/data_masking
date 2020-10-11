# data_masking
  
  Data masking is a data security technique in which a dataset is copied but with sensitive data obfuscated. This benign replica is then used instead of the authentic data for testing or training purposes.
  
What do I need to know about data masking?
Data masking does not just replace sensitive data with blanks. It creates characteristically intact, but inauthentic, replicas of personally identifiable data or other highly sensitive data in order to uphold the complexity and unique characteristics of data. In this way, tests performed on properly masked data will yield the same results as they would on the authentic dataset.

What are the benefits of data masking?
Data masking is essential in many regulated industries where personally identifiable information must be protected from overexposure. By masking data, the organization can expose the data as needed to test teams or database administrators without compromising the data or getting out of compliance. The primary benefit is reduced security risk.

We have use 3 different techniques to achieve this:
  1. Substitution: This technique effectively mimics the looks and feel of the real data without compromisisng anyones personal information.
  2. Shuffling: The data in a column is shuffelled in randomized fashion.
  3. Scrambling: In this technique charcters are jumbeled into a randonm order(word by word) so the original content is not revealed.
  
  for more details: https://en.wikipedia.org/wiki/Data_masking
