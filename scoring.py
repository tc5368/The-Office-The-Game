def save_scores(arr):
    f = open('scores.txt','w')
    f.write(str(arr))
    f.close()

def load_scores():
	f = open('scores.txt','r')
	data = f.read()
	f.close()
	if data == '':
		return []
	return eval(data)



def bubble_sort_score_section(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if int(arr[j].split()[0]) > int(arr[j+1].split()[0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

new = load_scores()
print(new)