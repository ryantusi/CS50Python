# take user input file name and split the file name and extension
file = input("File: ").lower().strip()
extn = file.split(".")

# Use conditionals to validate the extension
match extn[len(extn) - 1]:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
