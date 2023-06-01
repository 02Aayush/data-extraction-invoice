from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.http import HttpResponse
from invoice_app.models import InvoiceData
from PyPDF2 import PdfReader
import pandas as pd

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_invoice')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        # Handle user registration
        # Extract username, password, and any other required fields from the request
        username = request.POST['username']
        password = request.POST['password']
        # Create a new user object and save it to the database
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('login')
    else:
        return render(request, 'signup.html')


#Function to Upload invoice and data extraction from file
@login_required
def upload_invoice(request):
    if request.method == 'POST':
        InvoiceData.objects.all().delete()
        #  the uploaded file is accessed using request.FILES['invoice_file'].
        uploaded_file = request.FILES['invoice_file']

        reader = PdfReader(uploaded_file)
        page = reader.pages[0]
        extracted_data = page.extract_text().split("\n")

        # Create list to store data items
        invoice_no = []
        inv_date = []
        place_of_supply = []
        doc_type = []
        customer_name = []
        location = []
        pnr_no = []
        bus_op_name = []
        origin = []
        destination = []
        bus_fare = []
        operator_disc = []
        total_tax_val = []
        cgst = []
        sgst = []
        total_inv_val = []


        # Get Invoice Number
        index = [i + 4 for i, x in enumerate(extracted_data) if x == "Invoice No."]
        invoice_no.append(extracted_data[index[0]])

        # Get Invoice Date
        index = [i + 4 for i, x in enumerate(extracted_data) if x == "Date"]
        inv_date.append(extracted_data[index[0]])
        # print(inv_date)

        # Get Place of Supply
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Place of Supply :"]
        place_of_supply.append(extracted_data[index[0]])
        # print(place_of_supply)

        # Get Document Type
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Document Type :"]
        doc_type.append(extracted_data[index[0]])
        # print(doc_type)

        # Get Customer Name
        index = [i + 2 for i, x in enumerate(extracted_data) if x == "Customer Name :"]
        customer_name.append(extracted_data[index[0]])
        # print(customer_name)

        # Get Location
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Location :"]
        location.append(extracted_data[index[0]])
        # print(location)

        # Get PNR No.
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "PNR No :"]
        pnr_no.append(extracted_data[index[0]])
        # print(pnr_no)

        # Get Bus operator number
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Bus Operator Name & Address :"]
        bus_op_name.append(extracted_data[index[0]])
        # print(bus_op_name)

        # Get Origin
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Origin :"]
        end_origin = [i for i, x in enumerate(extracted_data[index[0]:]) if x == "Rescheduling Excess fare"]
        origin_str = ""
        for item in extracted_data[index[0]:index[0] + end_origin[0]]:
            origin_str = origin_str + item
        origin.append(origin_str)
        # print(origin)

        # Get Destination
        index = [i + 3 for i, x in enumerate(extracted_data) if x == "Destination :"]
        destination.append(extracted_data[index[0]])
        # print(destination)

        # Get Bus fare
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "Bus Fare"]
        bus_fare.append(extracted_data[index[0]])
        # print(bus_fare)

        # Get Operator Discount
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "Operator discount"]
        operator_disc.append(extracted_data[index[0]])
        # print(operator_disc)

        # Get Total Taxable Value
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "Total Taxable Value"]
        total_tax_val.append(extracted_data[index[0]])
        # print(total_tax_val)

        # Get CGST
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "CGST @ 2.5%"]
        cgst.append(extracted_data[index[0]])
        # print(cgst)

        # Get SGST
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "SGST @ 2.5%"]
        sgst.append(extracted_data[index[0]])
        # print(sgst)

        # Get Total Taxable Value
        index = [i + 1 for i, x in enumerate(extracted_data) if x == "Total Invoice Value"]
        total_inv_val.append(extracted_data[index[0]])
        # print(total_inv_val)

        df = pd.DataFrame({'Invoice No.': invoice_no,
                             'Invoice Date': inv_date,
                             'Place of Supply': place_of_supply,
                             'Doc Type': doc_type,
                             'Customer Name': customer_name,
                             'Location': location,
                             'PNR No.': pnr_no,
                             'Buss Operator Name & Address': bus_op_name,
                             'Origin': origin,
                             'Destination': destination,
                             'Buss Fare': bus_fare,
                             'Operator Discount': operator_disc,
                             'Total Tax Value': total_tax_val,
                             'CGST': cgst,
                             'SGST': sgst,
                             'Total Invoice Value': total_inv_val})

        # df.to_csv("data.csv", index=False)


        # Save the extracted data to the database
        # After extracting the data, an instance of the InvoiceData model is created, and the extracted data is assigned
        # to the data field. Calling invoice_data.save() saves the instance to the database
        invoice_data = InvoiceData(data=extracted_data)
        invoice_data.save()


        # Save the extracted data to a CSV file
        filename = 'extracted_data.csv'
        save_to_csv(df, filename)



        # It renders the invoice_details.html template, passing the extracted data as the data context variable.
        return render(request, 'invoice_details.html', {'data': extracted_data})

    return render(request, 'upload_invoice.html')


# function to retrieve and display the stored invoice data
@login_required
def invoice_details(request):
    invoices = InvoiceData.objects.all()   # Working
    # the InvoiceData.objects.all() retrieves all the stored invoices from the database. The retrieved data is then
    # passed to the invoice_list.html template, where you can display it as desired.
    return render(request, 'invoice_list.html', {'invoices': invoices})


# function to save data to CSV
def save_to_csv(data, filename):

    data.to_csv(filename, index=False, encoding='utf-8-sig')


# function to retrieve the file from the provided path and return it as response
@login_required
def download_csv(request, csv_file_path):
    with open(csv_file_path, 'rb') as file:

        # By setting the charset parameter to 'utf-8' in the content_type header, it ensures that the CSV file is served
        # with the correct encoding.
        response = HttpResponse(file, content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="extracted_data.csv"'
        return response


def logout_view(request):
    logout(request)
    return redirect('login')
