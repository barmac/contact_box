from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from contacts.models import *

# Create your views here.
class PersonList(View):
    
    def get(self, request):
        response = HttpResponse("<table>")
        for person in Person.objects.all().order_by('last_name'):
            response.write("""
            <tr>
              <td><a href="{id}">{first_name}</a></td>
              <td>{last_name}</td>
              <td>{description}</td>
              <td><a href="edit/{id}">Edit</a></td>
              <td><a href="delete/{id}">Delete</a></td>
            </tr>
            """.format(first_name=person.first_name, last_name=person.last_name, description=person.description, id=person.pk))
        response.write("""
        </table>
        <form action="add" method="get">
          <button type="submit">Add new person</button> 
        </form>
        """)
        return response
    

class ShowPerson(View):
    
    def get(self, request, id):
        response = HttpResponse("<table>")
        person = Person.objects.get(pk=id)
        response.write("""
        <ul>
          <li>First name: {first_name}</li>
          <li>Last name: {last_name}</li>
          <li>Description: {description}</li>
          <li>Phone number(s):</li>
          <ul>
        """.format(first_name=person.first_name, last_name=person.last_name, description=person.description))
        for phone in Phone.objects.filter(person=person):
            response.write("<li>{number} ({type})</li>".format(number=phone.number, type=phone.type))
        response.write("</ul><li>E-mail(s):</li><ul>")
        for email in Email.objects.filter(person=person):
            response.write("<li>{email}</li>".format(email=email.email))
        response.write("</ul><li>Address(es):</li><ul>")
        for address in Address.objects.filter(person=person):
            response.write("<li>{street} {house_no}{flat_no}, {city}</li>".format(street=address.street, house_no=address.house_no, flat_no="/{}".format(address.flat_no) if address.flat_no else "", city=address.city))
        response.write("</ul><li>Groups:</li><ul>")
        for group in person.group_set.all():
            response.write("<li>{name}</li>".format(name=group.name))
        response.write("""
          </ul>
          <li><a href="/edit/{id}">Edit</a></li>
          <li><a href="/delete/{id}">Delete</a></li>
        </tr>
        </table>
        """.format(id=id))
        return response


class AddPerson(View):
    
    def get(self, request):
        response = HttpResponse("""
        <form action="" method="POST">
          <input type="text" name="first_name" placeholder="First name">
          <input type="text" name="last_name" placeholder="Last name">
          <input type="text" name="description" placeholder="Description">
          <input type="submit" name="submit" value="Send">
        </form>
        """)
        return response
    
    def post(self, request): 
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")
        a = Person.objects.create(first_name=first_name, last_name=last_name, description=description)
        return redirect("/{id}".format(id=a.pk))


class EditPerson(View):
    
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        response = HttpResponse("""
        <form action="" method="POST">
          <input type="text" name="first_name" placeholder="First name" value={first_name}>
          <input type="text" name="last_name" placeholder="Last name" value={last_name}>
          <input type="text" name="description" placeholder="Description" value={description}>
          <input type="submit" name="submit" value="Send">
        </form>
        """.format(first_name=person.first_name, last_name=person.last_name, description=person.description))
        return response
    
    def post(self, request, id): 
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")
        person = Person.objects.get(pk=id)
        person.first_name = first_name
        person.last_name = last_name
        person.description = description
        person.save()
        return redirect("/")


class DeletePerson(View):
    
    def get(self, request, id):
        Person.objects.get(pk=id).delete()
        return redirect("/")