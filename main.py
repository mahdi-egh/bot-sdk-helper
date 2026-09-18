import sys
import sdkHelper
helper = sdkHelper.sdkHelper()
def main():
    if len(sys.argv)<2:
        print("missing method")
        return
    inputRequest = sys.argv[1]
    
    token = "696988573:zwApZSZMLYtkRdgHECpYOkuU8NchkYgVjbE"

    match inputRequest:
        case "sendMessage":
            chat_id = sys.argv[2]
            text = sys.argv[3]
            requst = helper.sendMessage(token,chat_id,text)
            print(requst)
            
        case "getMe":
            print(helper.getMe(token))

        case "getUpdates":
            print(helper.getUpdates(token))
if __name__ == '__main__':
    main()