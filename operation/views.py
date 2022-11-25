from django.shortcuts import render

# Create your views here.

def spares_main(request):
    return render(request, 'spares/spares_main.html')


def defects_main(request):
    defects = [
        {
            'vessel': 'Jet 2',
            'title': 'Leaking SB Outer ME SW cooling pump',
            'date_when_found': '15/11/2022',
            'date_when_closed': '',
            'status': 'Open'
        },
        {
            'vessel': 'Jet 2',
            'title': 'Leaking PS Outer ME SW cooling pump',
            'date_when_found': '18/11/2022',
            'date_when_closed': '',
            'status': 'Open'
        },
        {
            'vessel': 'Jet 1',
            'title': 'STB alternator breakdown',
            'date_when_found': '25/09/2022',
            'date_when_closed': '',
            'status': 'Open'
        }
    ]
    return render(request, 'defects/defects_main.html', {
            'defects': defects 
    })