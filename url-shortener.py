import hashlib

def shorten_url(url):
  # generate hash of the URL
  hash = hashlib.sha1(url.encode()).hexdigest()[:6]

  # create short URL using the hash
  short_url = "https://your_domain.com/" + hash

  return short_url