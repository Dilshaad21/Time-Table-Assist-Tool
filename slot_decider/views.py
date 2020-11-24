from django.shortcuts import render
from .forms import UploadFileForm
from .func import slot_allot
# Create your views here.


def file_upload(request):
    if request.method == 'POST':    # POST method in the case of the files submission
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # Files stored in a list format
            files = request.FILES.getlist('file_field')
            if(files[1].name == 'class.csv'):
                files[::-1]
            d = slot_allot(files[1], files[0])
            slots = []  # This list will contain all the slot names that need to be passed to the templates
            colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'yellow',
                      4: 'orange', 5: 'violet', 6: 'pink', 7: 'purple'}  # Color coding for slots
            i = 0
            hh = 0
            lunch = ['L', 'U', 'N', 'C', 'H']
            for x in d:
                j = 0
                dd = []
                for xx in x:
                    if(j == 4):
                        dd.append([lunch[hh], 'white'])
                    dd.append([chr(ord('A')+xx), colors[xx]])
                    j += 1
                slots.append(dd)
                i += 1
                hh += 1
            print(slots)
            courses_mat = [['c1', 'c2', 'c3'], ['c1', 'c2', 'c3'], ['c1', 'c2', 'c3'], ['c1', 'c2', 'c3'], [
                'c1', 'c2', 'c3'], ['c1', 'c2', 'c3'], ['c1', 'c2', 'c3'], ['c1', 'c2', 'c3']]
            courses = []
            i = 0
            for x in courses_mat:
                courses.append([x, colors[i]])
                i += 1

            # Each slot list passed for each day in a week
            course_table = {'Slot A': courses[0], 'Slot B': courses[1], 'Slot C': courses[2],
                            'Slot D': courses[3], 'Slot E': courses[4], 'Slot F': courses[5],
                            'Slot G': courses[6], 'Slot H': courses[7]}

            context = {'slot_table': {'Monday': slots[0], 'Tuesday': slots[1],
                                      'Wednesday': slots[2], 'Thursday': slots[3], 'Friday': slots[4]},
                       'course_table': course_table,
                       }
            # render time-table for post request after file is uploaded
            return render(request, 'time-table.html', context)
    else:
        form = UploadFileForm()
    # render form.html when get request is done
    return render(request, 'form.html', {'form': form})


def time_table(request):
    print('worked!')
    return render(request, 'time-table.html')
