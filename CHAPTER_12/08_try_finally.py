def main():

    try:
      a = int(input("Hey, Enter a no. "))
      print(a)
      return

    except Exception as e:
      print(e)
      return

    finally:
        print("i am inside of finally")

main()
