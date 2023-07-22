import base64
from email.message import EmailMessage
from email.mime.text import MIMEText

from django.conf import settings
from .models import Invitation


def send_invitation(to: str, sender: str, invitation: Invitation):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """

    register_link = settings.FE_HOST + '/invitations/'+str(invitation.id)

    content = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>

    <body>
        <div class="flex flex-col container mx-auto w-[35rem] border border-[#D8D8D8] my-5 rounded-2xl px-8 py-5" style="margin-left: auto; margin-right: auto; margin-top: 20px; margin-bottom: 20px; display: flex; width: 35rem; flex-direction: column; border-radius: 1rem; border-width: 1px; border-color: #D8D8D8; padding-left: 32px; padding-right: 32px; padding-top: 20px; padding-bottom: 20px;">
            <div>
                <svg width="60" viewBox="0 0 92 67" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_62_24455)">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M22.9558 62.7468L16.3107 25.3115L70.3617 15.7163L77.0068 53.1516L22.9558 62.7468ZM28.5468 31.2118C28.4536 30.6876 27.9533 30.3377 27.429 30.4312L24.5205 30.9474C23.9963 31.0406 23.6467 31.541 23.7399 32.0652C23.8229 32.5323 24.2293 32.8609 24.688 32.8609C24.7439 32.8609 24.8005 32.856 24.8576 32.846L27.7662 32.3298C28.2902 32.2366 28.6397 31.7362 28.5468 31.2118ZM30.1525 40.2579C30.0593 39.7337 29.559 39.3839 29.0347 39.4773L26.1269 39.9935C25.6027 40.0867 25.2532 40.5871 25.3463 41.1113C25.4293 41.5786 25.836 41.9071 26.2944 41.9071C26.3503 41.9071 26.4069 41.9021 26.4641 41.8921L29.3719 41.3759C29.8961 41.2825 30.2457 40.7821 30.1525 40.2579ZM31.8986 50.2153C31.8054 49.6911 31.305 49.3412 30.7808 49.4347L27.873 49.9509C27.3488 50.0441 26.9992 50.5445 27.0924 51.0687C27.1754 51.5358 27.5821 51.8644 28.0405 51.8644C28.0964 51.8644 28.153 51.8595 28.2102 51.8495L31.118 51.3333C31.6422 51.2401 31.9917 50.7395 31.8986 50.2153ZM37.8433 29.5616C37.7502 29.0374 37.25 28.6876 36.7256 28.781L33.817 29.2973C33.2928 29.3904 32.9433 29.8908 33.0364 30.415C33.1194 30.8821 33.5259 31.2108 33.9845 31.2108C34.0404 31.2108 34.097 31.2058 34.1542 31.1959L37.0627 30.6796C37.5867 30.5862 37.9362 30.0858 37.8433 29.5616ZM39.449 38.6075C39.3559 38.0832 38.8557 37.7334 38.3313 37.8269L35.4227 38.3434C34.8985 38.4365 34.549 38.9369 34.6421 39.4611C34.7251 39.9282 35.1316 40.2569 35.5902 40.2569C35.6461 40.2569 35.7027 40.2519 35.7599 40.242L38.6684 39.7255C39.1926 39.632 39.5422 39.1317 39.449 38.6075ZM41.5931 45.6581C41.1536 45.3577 40.5536 45.4705 40.2532 45.91L39.1469 47.5293L37.5509 46.39C37.1176 46.0804 36.5154 46.181 36.2061 46.6143C35.8968 47.0479 35.9971 47.6498 36.4304 47.9591L38.059 49.1216L36.9303 50.7738C36.6299 51.2133 36.743 51.8133 37.1827 52.1136C37.3489 52.2274 37.5382 52.2818 37.7256 52.2818C38.0334 52.2818 38.3358 52.1348 38.5226 51.8615L39.6289 50.2424L41.2252 51.382C41.3948 51.5032 41.5906 51.5613 41.7844 51.5613C42.0853 51.5613 42.3817 51.421 42.57 51.1574C42.8793 50.7238 42.7787 50.1219 42.3454 49.8125L40.7168 48.6501L41.8455 46.9982C42.1454 46.5584 42.0326 45.9587 41.5931 45.6581ZM47.1391 27.9119C47.0462 27.3877 46.5458 27.0384 46.0216 27.1311L43.1131 27.6468C42.5889 27.7398 42.2393 28.2401 42.3322 28.7646C42.4152 29.2319 42.8217 29.5604 43.2803 29.5604C43.3362 29.5604 43.3928 29.5554 43.4497 29.5455L46.3583 29.0297C46.8825 28.9365 47.2323 28.4362 47.1391 27.9119ZM48.7448 36.957C48.6516 36.4328 48.1513 36.083 47.6271 36.1764L44.7188 36.693C44.1946 36.7861 43.845 37.2865 43.9382 37.8107C44.0211 38.2778 44.4276 38.6065 44.8862 38.6065C44.9421 38.6065 44.9988 38.6015 45.0559 38.5916L47.9642 38.075C48.4884 37.9819 48.838 37.4813 48.7448 36.957ZM50.9893 45.8471L48.0807 46.3636C47.5565 46.4568 47.2069 46.9572 47.3001 47.4814C47.3831 47.9487 47.7895 48.2772 48.2482 48.2772C48.3041 48.2772 48.3607 48.2722 48.4179 48.2622L51.3264 47.7457C51.8506 47.6526 52.2002 47.1522 52.107 46.628C52.0141 46.1035 51.5137 45.754 50.9893 45.8471ZM56.4352 26.2613C56.342 25.7371 55.8419 25.3872 55.3174 25.4807L52.4089 25.9969C51.8847 26.0901 51.5351 26.5905 51.6283 27.1147C51.7112 27.5818 52.1177 27.9104 52.5763 27.9104C52.6322 27.9104 52.6889 27.9055 52.746 27.8955L55.6545 27.3793C56.1788 27.2861 56.5283 26.7855 56.4352 26.2613ZM58.0409 35.3069C57.9479 34.7827 57.4473 34.4329 56.9231 34.5263L54.0146 35.0428C53.4903 35.136 53.1408 35.6363 53.234 36.1605C53.3169 36.6276 53.7234 36.9563 54.182 36.9563C54.2379 36.9563 54.2946 36.9513 54.3517 36.9414L57.26 36.4249C57.7845 36.3315 58.134 35.8308 58.0409 35.3069ZM60.65 45.1112C60.5568 44.587 60.0567 44.2375 59.5323 44.3306L56.6245 44.8469C56.1003 44.9401 55.7507 45.4404 55.8439 45.9646C55.9268 46.432 56.3333 46.7604 56.7919 46.7604C56.8478 46.7604 56.9045 46.7554 56.9616 46.7455L59.8694 46.2292C60.3936 46.1358 60.7429 45.6355 60.65 45.1112ZM65.7312 24.6111C65.638 24.0869 65.1377 23.7373 64.6134 23.8305L61.7057 24.347C61.1814 24.4402 60.8319 24.9405 60.925 25.4648C61.008 25.9321 61.4145 26.2603 61.8731 26.2603C61.929 26.2603 61.9857 26.2553 62.0428 26.2454L64.9506 25.7289C65.4748 25.6357 65.8244 25.1351 65.7312 24.6111ZM67.3369 33.6565C67.2437 33.1322 66.7436 32.7829 66.2191 32.8759L63.3113 33.3921C62.7871 33.4853 62.4376 33.9857 62.5307 34.5099C62.6137 34.9769 63.0202 35.3056 63.4788 35.3056C63.5347 35.3056 63.5913 35.3007 63.6485 35.2907L66.5563 34.7742C67.0805 34.681 67.4301 34.1807 67.3369 33.6565ZM69.1043 43.6111C69.0112 43.0869 68.511 42.7374 67.9866 42.8303L65.078 43.346C64.5538 43.439 64.2043 43.9393 64.2972 44.4635C64.3802 44.9309 64.7866 45.2593 65.2452 45.2593C65.3011 45.2593 65.3578 45.2543 65.4147 45.2444L68.3232 44.7286C68.8474 44.6357 69.1972 44.1353 69.1043 43.6111Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M26.0547 14.6653L24.5398 6.13858L21.3384 6.70736L22.8533 15.2341L26.0547 14.6653Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21.5554 17.1632C21.7651 17.3098 22.026 17.3667 22.2759 17.3219L27.3745 16.4164C27.8987 16.3232 28.2483 15.8228 28.1551 15.2986L27.4227 11.1739L55.0614 6.26742L55.7938 10.3923C55.8845 10.9195 56.3997 11.2679 56.9115 11.1729L62.0096 10.2679C62.2613 10.2231 62.4851 10.0803 62.6315 9.8706C62.7778 9.66091 62.8352 9.40179 62.7902 9.15011L62.0578 5.02544L68.2677 3.9231L70.0244 13.8181L15.9734 23.4133L14.2166 13.5183L20.426 12.4159L21.1584 16.5413C21.2031 16.793 21.346 17.0168 21.5554 17.1632Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M75.5674 58.1843L75.081 55.4464L25.4593 64.2624L25.9458 67.0003L75.5674 58.1843Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M60.7021 8.52734L59.1872 0.000160712L55.9863 0.568849L57.5012 9.09603L60.7021 8.52734Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M84.33 28.7111C85.2704 28.4938 89.3185 27.6168 90.3928 27.3626C90.9113 27.2399 91.4303 27.5606 91.553 28.0789C91.6755 28.5971 91.355 29.1164 90.8367 29.2391C89.7448 29.4975 85.6917 30.3755 84.7643 30.5899C84.6912 30.6068 84.6182 30.615 84.5464 30.615C84.1076 30.615 83.7109 30.3134 83.608 29.8677C83.488 29.3489 83.8112 28.8311 84.33 28.7111Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M81.6828 21.5087C82.0614 21.2163 84.7791 19.097 85.7674 18.3703C86.1963 18.0548 86.7997 18.147 87.1153 18.5758C87.4308 19.0049 87.3386 19.6081 86.9098 19.9236C85.9436 20.6342 83.2425 22.7405 82.8614 23.0346C82.686 23.17 82.4785 23.2359 82.2728 23.2359C81.9844 23.2359 81.6992 23.1069 81.5091 22.861C81.1834 22.4396 81.2614 21.8342 81.6828 21.5087Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M84.8365 36.1398C85.7647 36.3361 89.7616 37.2437 90.8175 37.4613C91.339 37.5689 91.6744 38.079 91.5668 38.6004C91.4729 39.0561 91.0714 39.3699 90.6237 39.3699C90.5591 39.3699 90.4936 39.3634 90.428 39.3498C89.3534 39.1281 85.3518 38.2196 84.4377 38.0263C83.9167 37.9162 83.5838 37.4047 83.6939 36.8837C83.8039 36.3627 84.3155 36.03 84.8365 36.1398Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M0.849816 43.2586C1.94769 43.1272 6.05074 42.5575 7.00701 42.438C7.53545 42.3719 8.01718 42.7465 8.08327 43.275C8.14935 43.8034 7.77445 44.2852 7.24626 44.3512C6.30317 44.469 2.19514 45.0397 1.07888 45.1731C1.04012 45.1778 1.00137 45.1801 0.963105 45.1801C0.481869 45.1801 0.0657272 44.8203 0.00709438 44.3304C-0.0562592 43.8017 0.321375 43.3219 0.849816 43.2586Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M6.72353 36.6471C6.62713 36.6471 6.52949 36.6327 6.43285 36.6021C5.96826 36.4553 2.70693 35.4076 1.56036 35.0744C1.04906 34.9259 0.754901 34.391 0.903471 33.8797C1.05204 33.3684 1.58719 33.0744 2.09824 33.2228C3.27065 33.5634 6.55186 34.6175 7.01371 34.7634C7.52128 34.9239 7.80277 35.4655 7.64252 35.973C7.51283 36.3845 7.13297 36.6471 6.72353 36.6471Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M3.92727 52.886C4.8485 52.3153 8.28896 50.0882 9.0882 49.5874C9.53938 49.3044 10.1344 49.441 10.4171 49.8922C10.6999 50.3434 10.5635 50.9384 10.1123 51.2211C9.32522 51.7145 5.88054 53.9443 4.94291 54.5252C4.78465 54.6231 4.6095 54.6698 4.43608 54.6698C4.11336 54.6698 3.79808 54.5078 3.61572 54.2134C3.33498 53.7605 3.4746 53.1665 3.92727 52.886Z" fill="#763F98"/>
                    </g>
                    <defs>
                        <clipPath id="clip0_62_24455">
                            <rect width="91.5865" height="67" fill="white"/>
                        </clipPath>
                    </defs>
                </svg>
                <div class="my-5 text-2xl font-semibold" style="margin-top: 20px; margin-bottom: 20px; font-size: 24px; font-weight: 600;">
                    Meeting confirmed!.
                </div>
                <div class="mb-5 text-xl font-semibold" style="margin-bottom: 20px; font-size: 20px; font-weight: 600;">
                    ''' + invitation.meeting.summary + '''
                </div>
                <div class="flex items-center pb-5 mb-2 border-b border-[#D8D8D8]" style="margin-bottom: 8px; display: flex; align-items: center; border-bottom-width: 1px; border-color: #D8D8D8; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <g clip-path="url(#clip0_64_24482)">
                                <path d="M10 4.99996V9.99996L13.3334 11.6666M18.3334 9.99996C18.3334 14.6023 14.6024 18.3333 10 18.3333C5.39765 18.3333 1.66669 14.6023 1.66669 9.99996C1.66669 5.39759 5.39765 1.66663 10 1.66663C14.6024 1.66663 18.3334 5.39759 18.3334 9.99996Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </g>
                            <defs>
                                <clipPath id="clip0_64_24482">
                                    <rect width="20" height="20" fill="white"/>
                                </clipPath>
                            </defs>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">WHEN</div>
                        <div class="font-semibold" style="font-weight: 600;">
                            ''' + invitation.meeting.start_date.strftime("%b %d %Y at %H:%M:%S") + ' - ' + invitation.meeting.end_date.strftime("%H:%M:%S") + ''' (MYT)
                        </div>
                    </div>
                </div>
                <div class="flex items-center pb-5 mb-2 border-b border-[#D8D8D8]" style="margin-bottom: 8px; display: flex; align-items: center; border-bottom-width: 1px; border-color: #D8D8D8; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <path d="M9.99998 10.8333C11.3807 10.8333 12.5 9.714 12.5 8.33329C12.5 6.95258 11.3807 5.83329 9.99998 5.83329C8.61927 5.83329 7.49998 6.95258 7.49998 8.33329C7.49998 9.714 8.61927 10.8333 9.99998 10.8333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M9.99998 18.3333C13.3333 15 16.6666 12.0152 16.6666 8.33329C16.6666 4.65139 13.6819 1.66663 9.99998 1.66663C6.31808 1.66663 3.33331 4.65139 3.33331 8.33329C3.33331 12.0152 6.66665 15 9.99998 18.3333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">WHERE</div>
                        <div class="font-semibold" style="font-weight: 600;">
                            ''' + invitation.meeting.venue.split(',')[0] + '''
                        </div>
                        <span>
                            ''' + invitation.meeting.venue.split(',').pop(0) + '''
                        </span>
                        <a href="#" class="block font-bold text-sm text-[#00A19C]" style="display: block; font-size: 14px; font-weight: 700; color: #00A19C;">
                            Get directions
                        </a>
                    </div>
                </div>
                <div class="flex items-center pb-5 mb-2" style="margin-bottom: 8px; display: flex; align-items: center; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <path d="M9.99998 10.8333C11.3807 10.8333 12.5 9.714 12.5 8.33329C12.5 6.95258 11.3807 5.83329 9.99998 5.83329C8.61927 5.83329 7.49998 6.95258 7.49998 8.33329C7.49998 9.714 8.61927 10.8333 9.99998 10.8333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M9.99998 18.3333C13.3333 15 16.6666 12.0152 16.6666 8.33329C16.6666 4.65139 13.6819 1.66663 9.99998 1.66663C6.31808 1.66663 3.33331 4.65139 3.33331 8.33329C3.33331 12.0152 6.66665 15 9.99998 18.3333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">MEET YOUR HOST</div>
                        <div class="flex my-2" style="margin-top: 8px; margin-bottom: 8px; display: flex;">
                            <img class="rounded-full mr-3" height="68" width="68" src="https://nordicapis.com/wp-content/uploads/Profile-Pic-Circle-Grey-Large-1.png" alt="img" style="margin-right: 12px; border-radius: 9999px;">
                            <div>
                                <div class="font-semibold mb-1" style="margin-bottom: 4px; font-weight: 600;">''' + invitation.host.name + '''</div>
                                <div class="text-sm mb-1" style="margin-bottom: 4px; font-size: 14px;">Your host will be notified <strong>automatically</strong> when you
                                    arrived</div>
                                <div class="flex mb-1" style="margin-bottom: 4px; display: flex;">
                                    <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                                        <path d="M6.54216 7.24889C7.12216 8.4569 7.91281 9.58911 8.91413 10.5904C9.91544 11.5917 11.0476 12.3824 12.2557 12.9624C12.3596 13.0123 12.4115 13.0372 12.4773 13.0564C12.7109 13.1245 12.9978 13.0756 13.1956 12.9339C13.2513 12.894 13.2989 12.8464 13.3942 12.7511C13.6855 12.4598 13.8312 12.3141 13.9777 12.2189C14.5301 11.8597 15.2422 11.8597 15.7947 12.2189C15.9411 12.3141 16.0868 12.4598 16.3781 12.7511L16.5405 12.9135C16.9834 13.3564 17.2048 13.5778 17.3251 13.8157C17.5644 14.2886 17.5644 14.8472 17.3251 15.3201C17.2048 15.558 16.9834 15.7794 16.5405 16.2223L16.4092 16.3536C15.9678 16.795 15.7471 17.0157 15.4471 17.1842C15.1142 17.3712 14.5971 17.5057 14.2153 17.5045C13.8711 17.5035 13.636 17.4368 13.1656 17.3033C10.6378 16.5858 8.25246 15.2321 6.26248 13.2421C4.27249 11.2521 2.91877 8.86679 2.20129 6.33896C2.06778 5.86858 2.00103 5.6334 2.00001 5.28928C1.99887 4.90742 2.13334 4.39035 2.32036 4.05743C2.4889 3.7574 2.70957 3.53672 3.15092 3.09537L3.28229 2.96401C3.72516 2.52114 3.94659 2.29971 4.18441 2.17942C4.65738 1.94019 5.21593 1.94019 5.6889 2.17942C5.92671 2.29971 6.14815 2.52114 6.59102 2.96401L6.75341 3.1264C7.04475 3.41774 7.19042 3.56341 7.28565 3.70989C7.64482 4.2623 7.64482 4.97445 7.28565 5.52686C7.19042 5.67334 7.04475 5.81901 6.75341 6.11035C6.65815 6.20561 6.61052 6.25324 6.57065 6.30891C6.42897 6.50677 6.38006 6.79365 6.44816 7.02728C6.46732 7.09303 6.49227 7.14498 6.54216 7.24889Z" stroke="#00A19C" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                    <span class="text-sm font-bold text-[#00A19C]" style="font-size: 14px; font-weight: 700; color: #00A19C;">''' + invitation.host.phone + '''</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="rounded-xl bg-[#EBF7F6] p-5 text-center mb-5" style="margin-bottom: 20px; border-radius: 0.75rem; background-color: #EBF7F6; padding: 20px; text-align: center;">
                    <div class="font-bold text-xl mb-4" style="margin-bottom: 16px; font-size: 20px; font-weight: 700;">Before you arrive</div>
                    <div class="mb-4 text-sm" style="margin-bottom: 16px; font-size: 14px;">Pre-register and skip the queue — It only takes 30 seconds</div>
                    <a type="button" href="''' + register_link + '''" target="_blank" class="no-underline w-full text-white bg-[#00A19C] hover:bg-[#00A19C] font-bold rounded-md text-sm px-5 py-3.5 mr-auto dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none " style="margin-right: auto; width: 100%; border-radius: 0.375rem; background-color: #00A19C; padding-left: 20px; padding-right: 20px; padding-top: 14px; padding-bottom: 14px; font-size: 14px; font-weight: 700; color: #fff; text-decoration-line: none;">Pre-Register
                        Here</a>
                </div>
                <div class="font-bold text-xl mb-4" style="margin-bottom: 16px; font-size: 20px; font-weight: 700;">Things to know</div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">DRESS CODE</div>
                    <div class="font-semibold" style="font-weight: 600;">Smart Casual. Strictly no shorts, collarless T-shirts, singlets, sports
                        attire, sports shoes or slippers at any time.</div>
                </div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">SAFETY BRIEFING</div>
                    <div class="font-semibold" style="font-weight: 600;">Watch the safety briefing <a href="#" class="
                            text-[#00A19C]" style="color: #00A19C;"><u>here</u></a></div>
                </div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">WI-FI DETAILS</div>
                    <div class="font-semibold" style="font-weight: 600;">Get your wi-fi pre-approved <a href="#" class="
                        text-[#00A19C]" style="color: #00A19C;"><u>here</u></a></div>
                </div>
                <div class="py-4" style="padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">FACILITIES & ACCESSIBILITY</div>
                    <div class="font-semibold" style="font-weight: 600;">Assistance for elderly and specially abled visitors are available.</div>
                    <a href="#" class="font-semibold text-[#00A19C]" style="font-weight: 600; color: #00A19C;">Learn more</a>
                </div>
            </div>
        </div>

    </body>



    </html>
    '''

    message = EmailMessage()
    message['to'] = to
    message['from'] = sender
    message['subject'] = 'Meeting Invitation:'

    message.add_header('Content-Type','text/html')
    message.set_payload(content)

    return {'raw': base64.urlsafe_b64encode(bytes(
                        message.as_string(),
                        "utf-8")).decode("utf-8")}



def confirmed_email(to:str, sender: str, invitation: Invitation):

    content = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>

    <body>
        <div class="flex flex-col container mx-auto w-[35rem] border border-[#D8D8D8] my-5 rounded-2xl px-8 py-5" style="margin-left: auto; margin-right: auto; margin-top: 20px; margin-bottom: 20px; display: flex; width: 35rem; flex-direction: column; border-radius: 1rem; border-width: 1px; border-color: #D8D8D8; padding-left: 32px; padding-right: 32px; padding-top: 20px; padding-bottom: 20px;">
            <div>
                <svg width="60" viewBox="0 0 92 67" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_62_24455)">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M22.9558 62.7468L16.3107 25.3115L70.3617 15.7163L77.0068 53.1516L22.9558 62.7468ZM28.5468 31.2118C28.4536 30.6876 27.9533 30.3377 27.429 30.4312L24.5205 30.9474C23.9963 31.0406 23.6467 31.541 23.7399 32.0652C23.8229 32.5323 24.2293 32.8609 24.688 32.8609C24.7439 32.8609 24.8005 32.856 24.8576 32.846L27.7662 32.3298C28.2902 32.2366 28.6397 31.7362 28.5468 31.2118ZM30.1525 40.2579C30.0593 39.7337 29.559 39.3839 29.0347 39.4773L26.1269 39.9935C25.6027 40.0867 25.2532 40.5871 25.3463 41.1113C25.4293 41.5786 25.836 41.9071 26.2944 41.9071C26.3503 41.9071 26.4069 41.9021 26.4641 41.8921L29.3719 41.3759C29.8961 41.2825 30.2457 40.7821 30.1525 40.2579ZM31.8986 50.2153C31.8054 49.6911 31.305 49.3412 30.7808 49.4347L27.873 49.9509C27.3488 50.0441 26.9992 50.5445 27.0924 51.0687C27.1754 51.5358 27.5821 51.8644 28.0405 51.8644C28.0964 51.8644 28.153 51.8595 28.2102 51.8495L31.118 51.3333C31.6422 51.2401 31.9917 50.7395 31.8986 50.2153ZM37.8433 29.5616C37.7502 29.0374 37.25 28.6876 36.7256 28.781L33.817 29.2973C33.2928 29.3904 32.9433 29.8908 33.0364 30.415C33.1194 30.8821 33.5259 31.2108 33.9845 31.2108C34.0404 31.2108 34.097 31.2058 34.1542 31.1959L37.0627 30.6796C37.5867 30.5862 37.9362 30.0858 37.8433 29.5616ZM39.449 38.6075C39.3559 38.0832 38.8557 37.7334 38.3313 37.8269L35.4227 38.3434C34.8985 38.4365 34.549 38.9369 34.6421 39.4611C34.7251 39.9282 35.1316 40.2569 35.5902 40.2569C35.6461 40.2569 35.7027 40.2519 35.7599 40.242L38.6684 39.7255C39.1926 39.632 39.5422 39.1317 39.449 38.6075ZM41.5931 45.6581C41.1536 45.3577 40.5536 45.4705 40.2532 45.91L39.1469 47.5293L37.5509 46.39C37.1176 46.0804 36.5154 46.181 36.2061 46.6143C35.8968 47.0479 35.9971 47.6498 36.4304 47.9591L38.059 49.1216L36.9303 50.7738C36.6299 51.2133 36.743 51.8133 37.1827 52.1136C37.3489 52.2274 37.5382 52.2818 37.7256 52.2818C38.0334 52.2818 38.3358 52.1348 38.5226 51.8615L39.6289 50.2424L41.2252 51.382C41.3948 51.5032 41.5906 51.5613 41.7844 51.5613C42.0853 51.5613 42.3817 51.421 42.57 51.1574C42.8793 50.7238 42.7787 50.1219 42.3454 49.8125L40.7168 48.6501L41.8455 46.9982C42.1454 46.5584 42.0326 45.9587 41.5931 45.6581ZM47.1391 27.9119C47.0462 27.3877 46.5458 27.0384 46.0216 27.1311L43.1131 27.6468C42.5889 27.7398 42.2393 28.2401 42.3322 28.7646C42.4152 29.2319 42.8217 29.5604 43.2803 29.5604C43.3362 29.5604 43.3928 29.5554 43.4497 29.5455L46.3583 29.0297C46.8825 28.9365 47.2323 28.4362 47.1391 27.9119ZM48.7448 36.957C48.6516 36.4328 48.1513 36.083 47.6271 36.1764L44.7188 36.693C44.1946 36.7861 43.845 37.2865 43.9382 37.8107C44.0211 38.2778 44.4276 38.6065 44.8862 38.6065C44.9421 38.6065 44.9988 38.6015 45.0559 38.5916L47.9642 38.075C48.4884 37.9819 48.838 37.4813 48.7448 36.957ZM50.9893 45.8471L48.0807 46.3636C47.5565 46.4568 47.2069 46.9572 47.3001 47.4814C47.3831 47.9487 47.7895 48.2772 48.2482 48.2772C48.3041 48.2772 48.3607 48.2722 48.4179 48.2622L51.3264 47.7457C51.8506 47.6526 52.2002 47.1522 52.107 46.628C52.0141 46.1035 51.5137 45.754 50.9893 45.8471ZM56.4352 26.2613C56.342 25.7371 55.8419 25.3872 55.3174 25.4807L52.4089 25.9969C51.8847 26.0901 51.5351 26.5905 51.6283 27.1147C51.7112 27.5818 52.1177 27.9104 52.5763 27.9104C52.6322 27.9104 52.6889 27.9055 52.746 27.8955L55.6545 27.3793C56.1788 27.2861 56.5283 26.7855 56.4352 26.2613ZM58.0409 35.3069C57.9479 34.7827 57.4473 34.4329 56.9231 34.5263L54.0146 35.0428C53.4903 35.136 53.1408 35.6363 53.234 36.1605C53.3169 36.6276 53.7234 36.9563 54.182 36.9563C54.2379 36.9563 54.2946 36.9513 54.3517 36.9414L57.26 36.4249C57.7845 36.3315 58.134 35.8308 58.0409 35.3069ZM60.65 45.1112C60.5568 44.587 60.0567 44.2375 59.5323 44.3306L56.6245 44.8469C56.1003 44.9401 55.7507 45.4404 55.8439 45.9646C55.9268 46.432 56.3333 46.7604 56.7919 46.7604C56.8478 46.7604 56.9045 46.7554 56.9616 46.7455L59.8694 46.2292C60.3936 46.1358 60.7429 45.6355 60.65 45.1112ZM65.7312 24.6111C65.638 24.0869 65.1377 23.7373 64.6134 23.8305L61.7057 24.347C61.1814 24.4402 60.8319 24.9405 60.925 25.4648C61.008 25.9321 61.4145 26.2603 61.8731 26.2603C61.929 26.2603 61.9857 26.2553 62.0428 26.2454L64.9506 25.7289C65.4748 25.6357 65.8244 25.1351 65.7312 24.6111ZM67.3369 33.6565C67.2437 33.1322 66.7436 32.7829 66.2191 32.8759L63.3113 33.3921C62.7871 33.4853 62.4376 33.9857 62.5307 34.5099C62.6137 34.9769 63.0202 35.3056 63.4788 35.3056C63.5347 35.3056 63.5913 35.3007 63.6485 35.2907L66.5563 34.7742C67.0805 34.681 67.4301 34.1807 67.3369 33.6565ZM69.1043 43.6111C69.0112 43.0869 68.511 42.7374 67.9866 42.8303L65.078 43.346C64.5538 43.439 64.2043 43.9393 64.2972 44.4635C64.3802 44.9309 64.7866 45.2593 65.2452 45.2593C65.3011 45.2593 65.3578 45.2543 65.4147 45.2444L68.3232 44.7286C68.8474 44.6357 69.1972 44.1353 69.1043 43.6111Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M26.0547 14.6653L24.5398 6.13858L21.3384 6.70736L22.8533 15.2341L26.0547 14.6653Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21.5554 17.1632C21.7651 17.3098 22.026 17.3667 22.2759 17.3219L27.3745 16.4164C27.8987 16.3232 28.2483 15.8228 28.1551 15.2986L27.4227 11.1739L55.0614 6.26742L55.7938 10.3923C55.8845 10.9195 56.3997 11.2679 56.9115 11.1729L62.0096 10.2679C62.2613 10.2231 62.4851 10.0803 62.6315 9.8706C62.7778 9.66091 62.8352 9.40179 62.7902 9.15011L62.0578 5.02544L68.2677 3.9231L70.0244 13.8181L15.9734 23.4133L14.2166 13.5183L20.426 12.4159L21.1584 16.5413C21.2031 16.793 21.346 17.0168 21.5554 17.1632Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M75.5674 58.1843L75.081 55.4464L25.4593 64.2624L25.9458 67.0003L75.5674 58.1843Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M60.7021 8.52734L59.1872 0.000160712L55.9863 0.568849L57.5012 9.09603L60.7021 8.52734Z" fill="#20C997"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M84.33 28.7111C85.2704 28.4938 89.3185 27.6168 90.3928 27.3626C90.9113 27.2399 91.4303 27.5606 91.553 28.0789C91.6755 28.5971 91.355 29.1164 90.8367 29.2391C89.7448 29.4975 85.6917 30.3755 84.7643 30.5899C84.6912 30.6068 84.6182 30.615 84.5464 30.615C84.1076 30.615 83.7109 30.3134 83.608 29.8677C83.488 29.3489 83.8112 28.8311 84.33 28.7111Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M81.6828 21.5087C82.0614 21.2163 84.7791 19.097 85.7674 18.3703C86.1963 18.0548 86.7997 18.147 87.1153 18.5758C87.4308 19.0049 87.3386 19.6081 86.9098 19.9236C85.9436 20.6342 83.2425 22.7405 82.8614 23.0346C82.686 23.17 82.4785 23.2359 82.2728 23.2359C81.9844 23.2359 81.6992 23.1069 81.5091 22.861C81.1834 22.4396 81.2614 21.8342 81.6828 21.5087Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M84.8365 36.1398C85.7647 36.3361 89.7616 37.2437 90.8175 37.4613C91.339 37.5689 91.6744 38.079 91.5668 38.6004C91.4729 39.0561 91.0714 39.3699 90.6237 39.3699C90.5591 39.3699 90.4936 39.3634 90.428 39.3498C89.3534 39.1281 85.3518 38.2196 84.4377 38.0263C83.9167 37.9162 83.5838 37.4047 83.6939 36.8837C83.8039 36.3627 84.3155 36.03 84.8365 36.1398Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M0.849816 43.2586C1.94769 43.1272 6.05074 42.5575 7.00701 42.438C7.53545 42.3719 8.01718 42.7465 8.08327 43.275C8.14935 43.8034 7.77445 44.2852 7.24626 44.3512C6.30317 44.469 2.19514 45.0397 1.07888 45.1731C1.04012 45.1778 1.00137 45.1801 0.963105 45.1801C0.481869 45.1801 0.0657272 44.8203 0.00709438 44.3304C-0.0562592 43.8017 0.321375 43.3219 0.849816 43.2586Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M6.72353 36.6471C6.62713 36.6471 6.52949 36.6327 6.43285 36.6021C5.96826 36.4553 2.70693 35.4076 1.56036 35.0744C1.04906 34.9259 0.754901 34.391 0.903471 33.8797C1.05204 33.3684 1.58719 33.0744 2.09824 33.2228C3.27065 33.5634 6.55186 34.6175 7.01371 34.7634C7.52128 34.9239 7.80277 35.4655 7.64252 35.973C7.51283 36.3845 7.13297 36.6471 6.72353 36.6471Z" fill="#763F98"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M3.92727 52.886C4.8485 52.3153 8.28896 50.0882 9.0882 49.5874C9.53938 49.3044 10.1344 49.441 10.4171 49.8922C10.6999 50.3434 10.5635 50.9384 10.1123 51.2211C9.32522 51.7145 5.88054 53.9443 4.94291 54.5252C4.78465 54.6231 4.6095 54.6698 4.43608 54.6698C4.11336 54.6698 3.79808 54.5078 3.61572 54.2134C3.33498 53.7605 3.4746 53.1665 3.92727 52.886Z" fill="#763F98"/>
                    </g>
                    <defs>
                        <clipPath id="clip0_62_24455">
                            <rect width="91.5865" height="67" fill="white"/>
                        </clipPath>
                    </defs>
                </svg>
                <div class="my-5 text-2xl font-semibold" style="margin-top: 20px; margin-bottom: 20px; font-size: 24px; font-weight: 600;">
                    Your meeting is confirmed.
                </div>
                <div class="flex flex-col items-center px-8 py-5 bg-[#EBF7F6] rounded-xl text-center mb-5" style="margin-bottom: 20px; display: flex; flex-direction: column; align-items: center; border-radius: 0.75rem; background-color: #EBF7F6; padding-left: 32px; padding-right: 32px; padding-top: 20px; padding-bottom: 20px; text-align: center;">
                    <div class="text-sm text-[#808080] font-semibold mb-2" style="margin-bottom: 8px; font-size: 14px; font-weight: 600; color: #808080;">SKIP THE QUEUE</div>
                    <div class="text-xl font-semibold mb-4" style="margin-bottom: 16px; font-size: 20px; font-weight: 600;">Show this QR at the lobby</div>
                    <div class="rounded-2xl" style="border-radius: 1rem;">
                        <img class="h-72 rounded-xl" src="''' + settings.FE_HOST + '/api/invitations/' + str(invitation.id) + '/qr/' + '''" alt="qr" style="height: 288px; border-radius: 0.75rem;">
                    </div>
                </div>
                <div class="mb-5 text-xl font-semibold" style="margin-bottom: 20px; font-size: 20px; font-weight: 600;">
                    ''' + invitation.meeting.summary + '''
                </div>
                <div class="flex items-center pb-5 mb-2 border-b border-[#D8D8D8]" style="margin-bottom: 8px; display: flex; align-items: center; border-bottom-width: 1px; border-color: #D8D8D8; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <g clip-path="url(#clip0_64_24482)">
                                <path d="M10 4.99996V9.99996L13.3334 11.6666M18.3334 9.99996C18.3334 14.6023 14.6024 18.3333 10 18.3333C5.39765 18.3333 1.66669 14.6023 1.66669 9.99996C1.66669 5.39759 5.39765 1.66663 10 1.66663C14.6024 1.66663 18.3334 5.39759 18.3334 9.99996Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </g>
                            <defs>
                                <clipPath id="clip0_64_24482">
                                    <rect width="20" height="20" fill="white"/>
                                </clipPath>
                            </defs>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">WHEN</div>
                        <div class="font-semibold" style="font-weight: 600;">
                            ''' + invitation.meeting.start_date.strftime("%b %d %Y at %H:%M:%S") + ' - ' + invitation.meeting.end_date.strftime("%H:%M:%S") + ''' (MYT)
                        </div>
                    </div>
                </div>
                <div class="flex items-center pb-5 mb-2 border-b border-[#D8D8D8]" style="margin-bottom: 8px; display: flex; align-items: center; border-bottom-width: 1px; border-color: #D8D8D8; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <path d="M9.99998 10.8333C11.3807 10.8333 12.5 9.714 12.5 8.33329C12.5 6.95258 11.3807 5.83329 9.99998 5.83329C8.61927 5.83329 7.49998 6.95258 7.49998 8.33329C7.49998 9.714 8.61927 10.8333 9.99998 10.8333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M9.99998 18.3333C13.3333 15 16.6666 12.0152 16.6666 8.33329C16.6666 4.65139 13.6819 1.66663 9.99998 1.66663C6.31808 1.66663 3.33331 4.65139 3.33331 8.33329C3.33331 12.0152 6.66665 15 9.99998 18.3333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">WHERE</div>
                        <div class="font-semibold" style="font-weight: 600;">
                            ''' + invitation.meeting.venue.split(',')[0] + '''
                        </div>
                        <span>
                            ''' + invitation.meeting.venue.split(',').pop(0) + '''
                        </span>
                        <a href="#" class="block font-bold text-sm text-[#00A19C]" style="display: block; font-size: 14px; font-weight: 700; color: #00A19C;">
                            Get directions
                        </a>
                    </div>
                </div>
                <div class="flex items-center pb-5 mb-2" style="margin-bottom: 8px; display: flex; align-items: center; padding-bottom: 20px;">
                    <div class="w-[20] h-[20]" style="height: 20; width: 20;">
                        <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                            <path d="M9.99998 10.8333C11.3807 10.8333 12.5 9.714 12.5 8.33329C12.5 6.95258 11.3807 5.83329 9.99998 5.83329C8.61927 5.83329 7.49998 6.95258 7.49998 8.33329C7.49998 9.714 8.61927 10.8333 9.99998 10.8333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M9.99998 18.3333C13.3333 15 16.6666 12.0152 16.6666 8.33329C16.6666 4.65139 13.6819 1.66663 9.99998 1.66663C6.31808 1.66663 3.33331 4.65139 3.33331 8.33329C3.33331 12.0152 6.66665 15 9.99998 18.3333Z" stroke="#758695" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                    <div>
                        <div class="text-xs font-semibold text-[#808080]" style="font-size: 12px; font-weight: 600; color: #808080;">MEET YOUR HOST</div>
                        <div class="flex my-2" style="margin-top: 8px; margin-bottom: 8px; display: flex;">
                            <img class="rounded-full mr-3 object-scale-down" width="50" src="https://nordicapis.com/wp-content/uploads/Profile-Pic-Circle-Grey-Large-1.png" alt="img" style="margin-right: 12px; border-radius: 9999px; -o-object-fit: scale-down; object-fit: scale-down;">
                            <div>
                                <div class="font-semibold mb-1" style="margin-bottom: 4px; font-weight: 600;">''' + invitation.host.name + '''</div>
                                <div class="text-sm mb-1" style="margin-bottom: 4px; font-size: 14px;">Your host will be notified <strong>automatically</strong> when you
                                    arrived</div>
                                <div class="flex mb-1" style="margin-bottom: 4px; display: flex;">
                                    <svg class="mr-3" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 12px;">
                                        <path d="M6.54216 7.24889C7.12216 8.4569 7.91281 9.58911 8.91413 10.5904C9.91544 11.5917 11.0476 12.3824 12.2557 12.9624C12.3596 13.0123 12.4115 13.0372 12.4773 13.0564C12.7109 13.1245 12.9978 13.0756 13.1956 12.9339C13.2513 12.894 13.2989 12.8464 13.3942 12.7511C13.6855 12.4598 13.8312 12.3141 13.9777 12.2189C14.5301 11.8597 15.2422 11.8597 15.7947 12.2189C15.9411 12.3141 16.0868 12.4598 16.3781 12.7511L16.5405 12.9135C16.9834 13.3564 17.2048 13.5778 17.3251 13.8157C17.5644 14.2886 17.5644 14.8472 17.3251 15.3201C17.2048 15.558 16.9834 15.7794 16.5405 16.2223L16.4092 16.3536C15.9678 16.795 15.7471 17.0157 15.4471 17.1842C15.1142 17.3712 14.5971 17.5057 14.2153 17.5045C13.8711 17.5035 13.636 17.4368 13.1656 17.3033C10.6378 16.5858 8.25246 15.2321 6.26248 13.2421C4.27249 11.2521 2.91877 8.86679 2.20129 6.33896C2.06778 5.86858 2.00103 5.6334 2.00001 5.28928C1.99887 4.90742 2.13334 4.39035 2.32036 4.05743C2.4889 3.7574 2.70957 3.53672 3.15092 3.09537L3.28229 2.96401C3.72516 2.52114 3.94659 2.29971 4.18441 2.17942C4.65738 1.94019 5.21593 1.94019 5.6889 2.17942C5.92671 2.29971 6.14815 2.52114 6.59102 2.96401L6.75341 3.1264C7.04475 3.41774 7.19042 3.56341 7.28565 3.70989C7.64482 4.2623 7.64482 4.97445 7.28565 5.52686C7.19042 5.67334 7.04475 5.81901 6.75341 6.11035C6.65815 6.20561 6.61052 6.25324 6.57065 6.30891C6.42897 6.50677 6.38006 6.79365 6.44816 7.02728C6.46732 7.09303 6.49227 7.14498 6.54216 7.24889Z" stroke="#00A19C" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                    <span class="text-sm font-bold text-[#00A19C]" style="font-size: 14px; font-weight: 700; color: #00A19C;">''' + invitation.host.phone + '''</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="font-semibold text-xl mb-4" style="margin-bottom: 16px; font-size: 20px; font-weight: 600;">Things to know</div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">DRESS CODE</div>
                    <div class="font-semibold" style="font-weight: 600;">Smart Casual. Strictly no shorts, collarless T-shirts, singlets, sports
                        attire, sports shoes or slippers at any time.</div>
                </div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">SAFETY BRIEFING</div>
                    <div class="font-semibold" style="font-weight: 600;">Watch the safety briefing <a href="#" class="
                            text-[#00A19C]" style="color: #00A19C;"><u>here</u></a></div>
                </div>
                <div class="py-4 border-b border-[#D8D8D8]" style="border-bottom-width: 1px; border-color: #D8D8D8; padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">WI-FI DETAILS</div>
                    <div class="font-semibold" style="font-weight: 600;">Get your wi-fi pre-approved <a href="#" class="
                        text-[#00A19C]" style="color: #00A19C;"><u>here</u></a></div>
                </div>
                <div class="py-4" style="padding-top: 16px; padding-bottom: 16px;">
                    <div class="text-sm font-semibold text-[#808080]" style="font-size: 14px; font-weight: 600; color: #808080;">FACILITIES & ACCESSIBILITY</div>
                    <div class="font-semibold" style="font-weight: 600;">Assistance for elderly and specially abled visitors are available.</div>
                    <a href="#" class="font-semibold text-[#00A19C]" style="font-weight: 600; color: #00A19C;">Learn more</a>
                </div>

            </div>
        </div>

    </body>

    </html>
    '''

    message = EmailMessage()
    message['to'] = to
    message['from'] = sender
    message['subject'] = 'Meeting Invitation:'

    message.add_header('Content-Type','text/html')
    message.set_payload(content)

    return {'raw': base64.urlsafe_b64encode(bytes(
                        message.as_string(),
                        "utf-8")).decode("utf-8")}