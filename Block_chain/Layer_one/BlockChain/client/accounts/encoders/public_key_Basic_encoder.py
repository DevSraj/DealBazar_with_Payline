 BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        """Counter to find Leading zeros """
        count = 0
        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break
        """ Convert to Numeric from Bytes """
        num = int.from_bytes(newAddr, "big")
        prefix = "1" * count

        result = ""

        """ BASE58 Encoding """
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result

        self.PublicAddress = prefix + result

        print(f"Private Key {self.privateKey}")
        print(f"Public Key {self.PublicAddress}")
        print(f"Xpoint {xpoint} \n Ypoint {ypoint}")
