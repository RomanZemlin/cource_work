import ssl

# проверка версии ssl
def check_ssl_version():
    ssl_version = ssl.OPENSSL_VERSION
    print("Версия SSL:", ssl_version)

check_ssl_version()
