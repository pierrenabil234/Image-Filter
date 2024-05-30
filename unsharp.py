import numpy as np
def unsharp_mask(img,k,blured):
  unsharp=np.zeros_like(blured)
  final=np.zeros_like(blured)
  ro,co=img.shape
#b3ml el img el aslia - blurry image we ba3diha bazwdo 3la el sora
  for r in range(ro):
    for c in range(co):
      unsharp[r][c]=img[r][c]-blured[r][c]

  for row in range(ro):
    for col in range(co):
      final[row][col]=img[row][col]+(k*unsharp[row][col])
      #k>1 yb2a esmo highboost filter
  return final