import requests
import hashlib
import sys

# the api requires a SHA1 hashed password. we can quickly generate
# such a hash using https://www.browserling.com/tools/sha1-hash
# password123 would be cbfdac6008f9cab4083784cbd1874f76618d2a97

# then it also uses a techique called k-Anonymity
# which takes the first 5 characters of the hashed pw
# we then get a response of the api with all known passwords starting with the
# hash (we never send OUR full password)


def request_api_data(query_char):

    # send first 5 char of SHA-1 hashed pasword to API
    # it will return a range of passwords starting with that sequence
    url = 'https://api.pwnedpasswords.com/range/' + query_char

    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the API and try again.")

    return response


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # the API works with SHA-1 hashed passwords, so convert
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # for the query we only need the first 5 characters, but we do need to split the string
    first5_char = sha1_password[:5]
    tail = sha1_password[5:]

    response = request_api_data(first5_char)

    # check if password exists in returned API response
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. Change it!")
        else:
            print(f"{password} was not found. Carry on!")
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
