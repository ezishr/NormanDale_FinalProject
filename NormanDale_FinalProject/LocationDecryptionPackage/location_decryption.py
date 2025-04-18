# location_decryption.py
import json

group_name = 'Norman Dale'
with open('Data/EncryptedGroupHints Spring 2025.json', 'r') as f:
    encrypted_data = json.load(f)



with open('Data/UCEnglish.txt', 'r') as f:
    uc_eng = f.readlines()


class LocationDecryption:
    """
    """
    
    def __init__(self, location_name, encrypted_data, uceng):
        """
        """
        self.location_name = location_name
        self.encrypted_data = encrypted_data
        self.uceng = uceng

    def decryption_location(self):
        """
        """

        # Get the encrypted data of the provided location.
        self.encrypted_location = self.encrypted_data[self.location_name]
        self.decryption_words = []

        # Loop through each encrypted data to get the UC English word and append in the decryption_words.
        for encryption in self.encrypted_location:
            self.decryption_words.append(self.uceng[int(encryption)].strip())

        # Join the words into a full sentence and print it.
        self.full_sentence = " ".join(self.decryption_words)
        print(self.full_sentence)

        return self.full_sentence

locationDecryption = LocationDecryption(location_name="Wilbur (Shooter) Flatch", encrypted_data=encrypted_data, uceng=uc_eng)
locationDecryption.decryption_location()