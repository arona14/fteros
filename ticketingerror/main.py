from pnr import Pnr,token,close_session
from ticketingerror import TicketingError
from mail import Mail, userEmail, customerEmail


p = Pnr()
t = TicketingError()
m = Mail()
list_pnr = p.list_of_pnr_in_q('124')
print(list_pnr)
cmd = 'QMOV/WR17124/WR1777'
p.send_sabre_entry(token, cmd)
for i in list_pnr:
    print(i)
    cmd = '*' + i
    resp1 = p.send_sabre_entry(token, cmd)
    cmd = '*QH'
    resp2 = p.send_sabre_entry(token, cmd)
    agent = t.get_agent(resp2)
    remarks = t.get_remarks(resp1)
    user_email = userEmail(agent['sign'])
    if user_email != None:
        m.sendMailUser(agent['sign'],i,remarks)
        print('sent')
    elif user_email == None:
        dk = t.get_dk(resp1)
        customer_email = m.customerEmail(dk)
        if customer_email != None:
            m.sendMailCustomer(dk,i,remarks)
            print('sent')
        elif customer_email == None:
            m.sendMailAdmin(i,remarks)
            print('sent')

close_session()