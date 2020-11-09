from django.shortcuts import render
from .forms import UploadFileForm
from .func import slot_allot
# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            files = request.FILES.getlist('file_field')
            d = slot_allot(files)
            slots = []
            colors = {0:'red', 1:'green', 2:'blue', 3:'yellow', 4:'orange', 5:'violet', 6:'pink'}
            i = 0
            for x in d:
                j = 0
                dd = []
                for xx in x:
                    if(i == 0 and j==3):
                        dd.append('L')
                    dd.append([chr(ord('A')+xx), colors[xx]])
                    j+=1
                slots.append(dd)
                i+=1
            print(slots)
            context = {'slot0': slots[0], 'slot1': slots[1],'slot2': slots[2],'slot3': slots[3],'slot4': slots[4],}
            return render(request,'time-table.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'form.html', {'form': form})


def time_table(request):
    print('worked!')
    return render(request, 'time-table.html')