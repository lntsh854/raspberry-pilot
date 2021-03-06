def int_rnd(x):
  return int(round(x))

def clip(x, lo, hi):
  return max(lo, min(hi, x))

def interp(x, xp, fp):
  N = len(xp)
  def get_interp(xv):
    hi = 0
    while hi < N and xv > xp[hi]:
      hi += 1
    low = hi - 1
    return fp[-1] if hi == N and xv > xp[low] else (
      fp[0] if hi == 0 else
      (xv - xp[low]) * (fp[hi] - fp[low]) / (xp[hi] - xp[low]) + fp[low])
  return [get_interp(v) for v in x] if hasattr(
    x, '__iter__') else get_interp(x)

def gernterp(x, xp, fp):
  if fp[1] > fp[0]:
    return max(fp[0], min(fp[1], (x - xp[0]) * (fp[1] - fp[0]) / (xp[1] - xp[0]) + fp[0]))
  else:
    return max(fp[1], min(fp[0], (x - xp[0]) * (fp[1] - fp[0]) / (xp[1] - xp[0]) + fp[0]))