#simple HashMap 충돌 O
"""
HashTableSize = 101 # prime number 약수가 없는 숫자를 사용하는게 일반적이다.
class SimpleHashMap:
    def __init__(self):
        self.hash_map = [None for h in range(HashTableSize)]
    def simple_hash(self, name): # 지금은 되게 단순한 hash value를 만듬
        sum = 0
        for ch in name:
            sum += ord(ch) # ord = ch의 아스키 코드 값을 돌려주는 함수
            # print(name, sum, sum%HashTableSize)
        # name 문자열의 각 문자 아스키 코드 값을 다 더함
        hash_value = sum % HashTableSize 
        return hash_value
    def put(self, name, tel_no):
        self.hash_map[self.simple_hash(name)] = tel_no
    def print_hash_map(self):
        for idx, value in enumerate(self.hash_map): # index랑 value를 같이 받아올수있다.
            if value is not None:
                print("{:>3} {:5>}".format(idx, value))
    def search(self, name):
        value = self.hash_map[self.simple_hash(name)]
        return value

HMap_telno = SimpleHashMap()
names = ["Kim Y-S", "Hong S-C", "Lee H-K", "Choi B-S", "ABCDEF", "CDEFAB"]
tel_numbers = [1234, 5678, 3456, 7890, 2468, 1357]
# put hash table
for i in range(len(names)):
    name = names[i]
    tel_no = tel_numbers[i]
    HMap_telno.put(name, tel_no)

HMap_telno.print_hash_map()

# search part
for idx in range(len(names)):
    name_to_search = names[idx]
    tel_no = HMap_telno.search(name_to_search)
    HMap_telno.search(name)
    print("tel_no of ({}) = {}".format(name_to_search, tel_no))

# 충돌이 일어남
"""
# HashMap_Bucket 충돌이 적어짐
class Entry:
    def __init__(self, k, v):
        self._key = k
        self._value = v
    def __str__(self):
        return str(self._value)

def CyclicShiftHashCode(str_key):
    mask = (1 << 32) -1
    h = 0
    for ch in str_key:
        h = (h<<5 & mask)|(h>>27) # cyclic shift hash code
        h += ord(ch)
    return h

class Bucket(Entry):
    def __init__(self):
        self._bucket=[]
    def _getitem(self, k):
        for item in self._bucket:
            if k == item._key:
                return item._value
        return None
    def _setitem(self, k, v):
        for item in self._bucket:
            if k == item._key:
                item._value = v
                return
        self._bucket.append(Entry(k,v)) # 버켓 안에 기존 항목이 없으면 추가
    def _delitem(self, k):
        for j in range(len(self._bucket)):
            if k == self._bucket[j]._key:
                self._bucket.pop(j)
                return 1
            return None
    def __len__(self):
        return len(self._bucket)
    def __iter__(self):
        for item in self._bucket:
            yield item._key
    
class HashMap_Bucket(Bucket):
    def __init__(self, table_size=11, prm=109345121):
        self._hash_tb1 = table_size*[None]
        self._hash_tb1_size = table_size
        self._num_entry=0
        self._prime = prm
    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime %self._hash_tb1_size
    def __len__(self):
        return self._num_entry
    def _getitem(self, k):
        hv = self._hash_value(k)
        #print("key({}) => hash_tbl[{}]".format(k, hv))
        bucket = self._hash_tb1[hv]
        return bucket._getitem(k)
    def _setitem(self, k, v):
        hv = self._hash_value(k)
        if self._hash_tb1[hv] is None:
            self._hash_tb1[hv] = Bucket()
        bucket = self._hash_tb1[hv]
        bucket._setitem(k, v)
        self._num_entry += 1
    def _delitem(self, k):
        hv = self._hash_value(k)
        bucket = self._hash_tb1[hv]
        bucket._delitem(k)
        self._num_entry -=1
    def __str__(self):
        s = ''
        for h in range(len(self._hash_tb1)):
            bucket = self._hash_tb1[h]
            if bucket is not None:
                s += "bucket[{:2d}] : ".format(h)
                for item in bucket:
                    s += str(item) + ",  "
                s+="\n "
        return s

####################################################
# main()

HashMap_Capacity = 7
print("Creating a HashMap_Bucket of capacity ({})".format(HashMap_Capacity))
hsMap = HashMap_Bucket(table_size= HashMap_Capacity)

student_records =  [("Leesuyoung", 21720943, "ICE", 4.5),("fsdfesfsd", 12345678, "EE", 4.3),
("sdjfkwodmk", 21720943, "MATH", 4.5),("sfsdfesd", 45678912, "IE", 4.4),
("adjqksjd", 21720943, "ENG", 4.5),("dofjwjkdk", 45689123, "CA", 4.5),
("zxjkadkm", 21720943, "FRA", 4.5),("sdifwjld", 15691234, "POL", 4.5),
("ajqjskd", 21720943, "MA", 4.5),("keyboard", 75342561, "SA", 4.5),
("qpdkemd", 21720943, "EL", 4.5),("machine", 78945612, "JA", 4.5),
("aoqsdmd", 21720943, "PT", 4.5),("mouse", 16789453, "PI", 4.5),
("zmaisfmd", 21720943, "PE", 4.5),("boomboom", 49532182, "SOC", 4.5),
("qijdkfjkd", 21720943, "PA", 4.5),("fsnmwoxd", 15684231, "SCI", 4.5),
("lleoele", 21720943, "MU", 4.5),("zxcqasd", 18962545, "MO", 4.5)]
for i in range(len(student_records)):
    st_record = student_records[i]
    st_name = st_record[0] # name = key
    hsMap._setitem(st_name, st_record)
print("Current HashMap Internal Structure : \n", hsMap)
for i in range(len(student_records)):
    st_name = student_records[i][0]
    st_record = hsMap._getitem(st_name)
    print("key {} : value {}".format(st_name, st_record))
st_name = "student_1"
st_record = hsMap._getitem(st_name)
if st_record == None:
    print("key ({}) : Value(This key don't exist in HashMap)".format(st_name))
else:
    print("key ({}) : Value ({})".format(st_name, st_record))
