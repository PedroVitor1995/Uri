# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def main():
	i = 0
	j = 1
	while True:

		if i > 2:
			break
		else:
			if i == 0:
				print('I=%.0f J=%.0f') % (i,j)
				print('I=%.0f J=%.0f') % (i,j+1)
				print('I=%.0f J=%.0f') % (i,j+2)
			elif i > 0 and i <= 0.9:
				print('I=%.1f J=%.1f') % (i,j)
				print('I=%.1f J=%.1f') % (i,j+1)
				print('I=%.1f J=%.1f') % (i,j+2)
			elif i == 1:
				print('I=%.0f J=%.0f') % (i,j)
				print('I=%.0f J=%.0f') % (i,j+1)
				print('I=%.0f J=%.0f') % (i,j+2)
			elif i > 1 and i < 1.9:
				print('I=%.1f J=%.1f') % (i,j)
				print('I=%.1f J=%.1f') % (i,j+1)
				print('I=%.1f J=%.1f') % (i,j+2)
			else:
				print('I=%.0f J=%.0f') % (i,j)
				print('I=%.0f J=%.0f') % (i,j+1)
				print('I=%.0f J=%.0f') % (i,j+2)
		i += 0.2
		j += 0.2
if __name__ == '__main__':
	main()