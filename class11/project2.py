print("Student App Access Manager")

CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

approved_apps = ["coding", "calculator", "notes"]
restricted_apps = ["gaming", "social media"]

student_name = input("Enter your name: ")
requested_app = input("Enter the app you want: ")

requested_app = requested_app.lower()

print(type(student_name) is str)
print(type(requested_app) is not int)

student_permissions = CAMERA | MICROPHONE | STORAGE

print("Permissions:", student_permissions)
print("Binary:", bin(student_permissions))

if student_permissions & CAMERA:
    print("Camera is enabled")

if student_permissions & MICROPHONE:
    print("Microphone is enabled")

if student_permissions & STORAGE:
    print("Storage is enabled")

print("Camera shifted left:", CAMERA << 1)
print("Storage shifted right:", STORAGE >> 1)

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted!")
else:
    print("Access denied!")