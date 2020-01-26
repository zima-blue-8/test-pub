def inc(x):
  return x + 1


def test_pass():
  assert inc(7) == 8

def test_fail():
  assert inc(3) == 5
