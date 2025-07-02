class PropertyUtil:
    @staticmethod
    def get_property_dict(file_path=r'D:\CaseStudy\db.properties'): # Change the File path if db.properties
        props = {}
        required_keys = ['host', 'port', 'dbname', 'user', 'password']

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if '=' not in line:
                    print(f"Skipping invalid line: {line}")
                    continue
                key, value = line.split('=', 1)
                props[key.strip()] = value.strip()

        for key in required_keys:
            if key not in props:
                raise KeyError(f"Missing required property: {key}")

        return {
            'host': props['host'],
            'port': int(props['port']),
            'database': props['dbname'],
            'user': props['user'],
            'password': props['password']
        }
