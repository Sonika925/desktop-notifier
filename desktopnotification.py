from plyer import notification
title = 'Bunny'
message= 'Good Evening !! Hope you all are well and doing good !!\n keep learning'
notification.notify(title= title,
                    message= message,
                    timeout= 10,
                    toast=False)