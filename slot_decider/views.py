from django.shortcuts import render
from .forms import UploadFileForm
from .func import slot_allot
# Create your views here.

def file_upload(request):
    if request.method == 'POST':    # POST method in the case of the files submission
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            files = request.FILES.getlist('file_field') # Files stored in a list format
            if(files[1].name=='class.csv'):
                files[::-1]
            d = slot_allot(files[1], files[0])
            slots = []  # This list will contain all the slot names that need to be passed to the templates
            colors = {0:'red', 1:'green', 2:'blue', 3:'yellow', 4:'orange', 5:'violet', 6:'pink'} # Color coding for slots
            i = 0
            for x in d:
                j = 0
                dd = []
                for xx in x:
                    if(i == 0 and j==4):
                        dd.append('L')
                    dd.append([chr(ord('A')+xx), colors[xx]])
                    j+=1
                slots.append(dd)
                i+=1
            print(slots)
            context = {'slot0': slots[0], 'slot1': slots[1],'slot2': slots[2],'slot3': slots[3],'slot4': slots[4],} # Each slot list passed for each day in a week
            return render(request,'time-table.html', context) # render time-table for post request after file is uploaded
    else:
        form = UploadFileForm()
    return render(request, 'form.html', {'form': form}) # render form.html when get request is done


def time_table(request):
    print('worked!')
    return render(request, 'time-table.html')