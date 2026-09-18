import sys
import sdkHelper
helper = sdkHelper.sdkHelper()
def main():
    inputRequest = sys.argv[1]
    print(sys.argv[2] if len(sys.argv)>2 else "")
    token = "696988573:zwApZSZMLYtkRdgHECpYOkuU8NchkYgVjbE"
    match inputRequest:
        case sendMessage:
            helper.sendMessage(token,chat_id,text)
    helper.sendMessage(token,"1786476947",'hiiiii')
if __name__ == '__main__':
    main()
# things that i must do:
    # get data by argv
    # remake match case 
