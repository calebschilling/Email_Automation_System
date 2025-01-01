def create_email_body():
    html_body = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
 <meta charset="UTF-8" />
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <!--[if !mso]><!-- -->
 <meta http-equiv="X-UA-Compatible" content="IE=edge" />
 <!--<![endif]-->
 <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 <meta name="format-detection" content="telephone=no" />
 <meta name="format-detection" content="date=no" />
 <meta name="format-detection" content="address=no" />
 <meta name="format-detection" content="email=no" />
 <meta name="x-apple-disable-message-reformatting" />
 <link href="https://fonts.googleapis.com/css?family=Poppins:ital,wght@0,300;0,400;0,400;0,500;0,600;0,800" rel="stylesheet" />
 <title>Sam Daily</title>
 <!-- Made with Postcards by Designmodo https://designmodo.com/postcards -->
 <style>
 html,
         body {
             margin: 0 !important;
             padding: 0 !important;
             min-height: 100% !important;
             width: 100% !important;
             -webkit-font-smoothing: antialiased;
         }
 
         * {
             -ms-text-size-adjust: 100%;
         }
 
         #outlook a {
             padding: 0;
         }
 
         .ReadMsgBody,
         .ExternalClass {
             width: 100%;
         }
 
         .ExternalClass,
         .ExternalClass p,
         .ExternalClass td,
         .ExternalClass div,
         .ExternalClass span,
         .ExternalClass font {
             line-height: 100%;
         }
 
         table,
         td,
         th {
             mso-table-lspace: 0 !important;
             mso-table-rspace: 0 !important;
             border-collapse: collapse;
         }
 
         u + .body table, u + .body td, u + .body th {
             will-change: transform;
         }
 
         body, td, th, p, div, li, a, span {
             -webkit-text-size-adjust: 100%;
             -ms-text-size-adjust: 100%;
             mso-line-height-rule: exactly;
         }
 
         img {
             border: 0;
             outline: 0;
             line-height: 100%;
             text-decoration: none;
             -ms-interpolation-mode: bicubic;
         }
 
         a[x-apple-data-detectors] {
             color: inherit !important;
             text-decoration: none !important;
         }
 
         .pc-gmail-fix {
             display: none;
             display: none !important;
         }
 
         .body .pc-project-body {
             background-color: transparent !important;
         }
 
         @media (min-width: 621px) {
             .pc-lg-hide {
                 display: none;
             } 
 
             .pc-lg-bg-img-hide {
                 background-image: none !important;
             }
         }
 </style>
 <style>
 @media (max-width: 620px) {
 .pc-project-body {min-width: 0px !important;}
 .pc-project-container {width: 100% !important;}
 .pc-sm-hide {display: none !important;}
 .pc-sm-bg-img-hide {background-image: none !important;}
 .pc-w620-padding-0-0-0-0 {padding: 0px 0px 0px 0px !important;}
 div.pc-w620-textAlign-center,th.pc-w620-textAlign-center,a.pc-w620-textAlign-center,td.pc-w620-textAlign-center {text-align: center !important;text-align-last: center !important;}
 table.pc-w620-textAlign-center {float: none !important;margin-right: auto !important;margin-left: auto !important;}
 img.pc-w620-textAlign-center {margin-right: auto !important;margin-left: auto !important;}
 .pc-w620-padding-8-16-8-16 {padding: 8px 16px 8px 16px !important;}
 table.pc-w620-spacing-0-0-0-0 {margin: 0px 0px 0px 0px !important;}
 td.pc-w620-spacing-0-0-0-0,th.pc-w620-spacing-0-0-0-0{margin: 0 !important;padding: 0px 0px 0px 0px !important;}
 .pc-w620-itemsSpacings-0-30 {padding-left: 0px !important;padding-right: 0px !important;padding-top: 15px !important;padding-bottom: 15px !important;}
 table.pc-w620-spacing-0-0-32-0 {margin: 0px 0px 32px 0px !important;}
 td.pc-w620-spacing-0-0-32-0,th.pc-w620-spacing-0-0-32-0{margin: 0 !important;padding: 0px 0px 32px 0px !important;}
 .pc-w620-fontSize-33px {font-size: 33px !important;}
 .pc-w620-lineHeight-120pc {line-height: 120% !important;}
 table.pc-w620-spacing-0-0-10-0 {margin: 0px 0px 10px 0px !important;}
 td.pc-w620-spacing-0-0-10-0,th.pc-w620-spacing-0-0-10-0{margin: 0 !important;padding: 0px 0px 10px 0px !important;}
 .pc-w620-fontSize-20px {font-size: 20px !important;}
 .pc-w620-fontSize-17px {font-size: 17px !important;}
 .pc-w620-lineHeight-133pc {line-height: 133% !important;}
 table.pc-w620-spacing-1-0-0-0 {margin: 1px 0px 0px 0px !important;}
 td.pc-w620-spacing-1-0-0-0,th.pc-w620-spacing-1-0-0-0{margin: 0 !important;padding: 1px 0px 0px 0px !important;}
 .pc-w620-padding-32-24-32-24 {padding: 32px 24px 32px 24px !important;}
 .pc-w620-padding-35-50-35-50 {padding: 35px 50px 35px 50px !important;}
 table.pc-w620-spacing-0-0-24-0 {margin: 0px 0px 24px 0px !important;}
 td.pc-w620-spacing-0-0-24-0,th.pc-w620-spacing-0-0-24-0{margin: 0 !important;padding: 0px 0px 24px 0px !important;}
 .pc-w620-fontSize-25px {font-size: 25px !important;}
 .pc-w620-itemsSpacings-0-32 {padding-left: 0px !important;padding-right: 0px !important;padding-top: 16px !important;padding-bottom: 16px !important;}
 .pc-w620-valign-bottom {vertical-align: bottom !important;}
 td.pc-w620-halign-center,th.pc-w620-halign-center {text-align: center !important;}
 table.pc-w620-halign-center {float: none !important;margin-right: auto !important;margin-left: auto !important;}
 img.pc-w620-halign-center {margin-right: auto !important;margin-left: auto !important;}
 table.pc-w620-spacing-0-0-20-0 {margin: 0px 0px 20px 0px !important;}
 td.pc-w620-spacing-0-0-20-0,th.pc-w620-spacing-0-0-20-0{margin: 0 !important;padding: 0px 0px 20px 0px !important;}
 .pc-w620-padding-20-24-32-24 {padding: 20px 24px 32px 24px !important;}
 .pc-w620-padding-15-30-15-30 {padding: 15px 30px 15px 30px !important;}
 
 .pc-w620-gridCollapsed-1 > tbody,.pc-w620-gridCollapsed-1 > tbody > tr,.pc-w620-gridCollapsed-1 > tr {display: inline-block !important;}
 .pc-w620-gridCollapsed-1.pc-width-fill > tbody,.pc-w620-gridCollapsed-1.pc-width-fill > tbody > tr,.pc-w620-gridCollapsed-1.pc-width-fill > tr {width: 100% !important;}
 .pc-w620-gridCollapsed-1.pc-w620-width-fill > tbody,.pc-w620-gridCollapsed-1.pc-w620-width-fill > tbody > tr,.pc-w620-gridCollapsed-1.pc-w620-width-fill > tr {width: 100% !important;}
 .pc-w620-gridCollapsed-1 > tbody > tr > td,.pc-w620-gridCollapsed-1 > tr > td {display: block !important;width: auto !important;padding-left: 0 !important;padding-right: 0 !important;}
 .pc-w620-gridCollapsed-1.pc-width-fill > tbody > tr > td,.pc-w620-gridCollapsed-1.pc-width-fill > tr > td {width: 100% !important;}
 .pc-w620-gridCollapsed-1.pc-w620-width-fill > tbody > tr > td,.pc-w620-gridCollapsed-1.pc-w620-width-fill > tr > td {width: 100% !important;}
 .pc-w620-gridCollapsed-1 > tbody > .pc-grid-tr-first > .pc-grid-td-first,pc-w620-gridCollapsed-1 > .pc-grid-tr-first > .pc-grid-td-first {padding-top: 0 !important;}
 .pc-w620-gridCollapsed-1 > tbody > .pc-grid-tr-last > .pc-grid-td-last,pc-w620-gridCollapsed-1 > .pc-grid-tr-last > .pc-grid-td-last {padding-bottom: 0 !important;}
 
 .pc-w620-gridCollapsed-0 > tbody > .pc-grid-tr-first > td,.pc-w620-gridCollapsed-0 > .pc-grid-tr-first > td {padding-top: 0 !important;}
 .pc-w620-gridCollapsed-0 > tbody > .pc-grid-tr-last > td,.pc-w620-gridCollapsed-0 > .pc-grid-tr-last > td {padding-bottom: 0 !important;}
 .pc-w620-gridCollapsed-0 > tbody > tr > .pc-grid-td-first,.pc-w620-gridCollapsed-0 > tr > .pc-grid-td-first {padding-left: 0 !important;}
 .pc-w620-gridCollapsed-0 > tbody > tr > .pc-grid-td-last,.pc-w620-gridCollapsed-0 > tr > .pc-grid-td-last {padding-right: 0 !important;}
 
 .pc-w620-tableCollapsed-1 > tbody,.pc-w620-tableCollapsed-1 > tbody > tr,.pc-w620-tableCollapsed-1 > tr {display: block !important;}
 .pc-w620-tableCollapsed-1.pc-width-fill > tbody,.pc-w620-tableCollapsed-1.pc-width-fill > tbody > tr,.pc-w620-tableCollapsed-1.pc-width-fill > tr {width: 100% !important;}
 .pc-w620-tableCollapsed-1.pc-w620-width-fill > tbody,.pc-w620-tableCollapsed-1.pc-w620-width-fill > tbody > tr,.pc-w620-tableCollapsed-1.pc-w620-width-fill > tr {width: 100% !important;}
 .pc-w620-tableCollapsed-1 > tbody > tr > td,.pc-w620-tableCollapsed-1 > tr > td {display: block !important;width: auto !important;}
 .pc-w620-tableCollapsed-1.pc-width-fill > tbody > tr > td,.pc-w620-tableCollapsed-1.pc-width-fill > tr > td {width: 100% !important;box-sizing: border-box !important;}
 .pc-w620-tableCollapsed-1.pc-w620-width-fill > tbody > tr > td,.pc-w620-tableCollapsed-1.pc-w620-width-fill > tr > td {width: 100% !important;box-sizing: border-box !important;}
 }
 @media (max-width: 520px) {
 .pc-w520-padding-30-40-30-40 {padding: 30px 40px 30px 40px !important;}
 .pc-w520-padding-15-25-15-25 {padding: 15px 25px 15px 25px !important;}
 }
 </style>
 <!--[if !mso]><!-- -->
 <style>
 @media all { @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 400; src: url('https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJnedA.woff') format('woff'), url('https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJnecg.woff2') format('woff2'); } @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 300; src: url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1JlEw.woff') format('woff'), url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1JlFQ.woff2') format('woff2'); } @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 600; src: url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1JlEw.woff') format('woff'), url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1JlFQ.woff2') format('woff2'); } @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 800; src: url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDD4Z1JlEw.woff') format('woff'), url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDD4Z1JlFQ.woff2') format('woff2'); } @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 500; src: url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlEw.woff') format('woff'), url('https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlFQ.woff2') format('woff2'); } }
 </style>
 <!--<![endif]-->
 <!--[if mso]>
    <style type="text/css">
        .pc-font-alt {
            font-family: Arial, Helvetica, sans-serif !important;
        }
    </style>
    <![endif]-->
 <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
</head>

<body class="body pc-font-alt" style="width: 100% !important; min-height: 100% !important; margin: 0 !important; padding: 0 !important; line-height: 1.5; color: #2D3A41; mso-line-height-rule: exactly; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-variant-ligatures: normal; text-rendering: optimizeLegibility; -moz-osx-font-smoothing: grayscale; background-color: #ffffff;" bgcolor="#ffffff">
 <table class="pc-project-body" style="table-layout: fixed; min-width: 600px; background-color: #ffffff;" bgcolor="#ffffff" width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
  <tr>
   <td align="center" valign="top">
    <table class="pc-project-container" align="center" width="600" style="width: 600px; max-width: 600px;" border="0" cellpadding="0" cellspacing="0" role="presentation">
     <tr>
      <td class="pc-w620-padding-0-0-0-0" style="padding: 20px 0px 20px 0px;" align="left" valign="top">
       <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="width: 100%;">
        <tr>
         <td valign="top">
          <!-- BEGIN MODULE: View in Browser -->
          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
           <tr>
            <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px;">
             <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
              <tr>
               <td valign="top" class="pc-w620-padding-8-16-8-16" style="padding: 8px 16px 8px 16px; border-radius: 0px; background-color: #d8d8d8;" bgcolor="#d8d8d8">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" class="pc-w620-textAlign-center" width="100%" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
                 <tr>
                  <td valign="top" class="pc-w620-textAlign-center" align="center">
                   <div class="pc-font-alt pc-w620-textAlign-center" style="line-height: 160%; letter-spacing: -0px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 12px; font-weight: 500; font-variant-ligatures: normal; color: #000000; text-align: center; text-align-last: center;">
                    <div><span>If you want to contact us now, </span><a href="mailto:schilling.caleb@yahoo.com" style="text-decoration: underline; color: red;">click here</a><span>.</span>

                    </div>
                   </div>
                  </td>
                 </tr>
                </table>
               </td>
              </tr>
             </table>
            </td>
           </tr>
          </table>
          <!-- END MODULE: View in Browser -->
         </td>
        </tr>
        <tr>
         <td valign="top">
          <!-- BEGIN MODULE: Header -->
          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
           <tr>
            <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px;">
             <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
              <tr>
               <td valign="top" class="pc-w620-padding-32-24-32-24" style="padding: 40px 32px 0px 32px; background-color: #000000;" bgcolor="#000000">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td class="pc-w620-spacing-0-0-32-0" style="padding: 0px 0px 8px 0px;">
                   <table class="pc-width-fill pc-w620-gridCollapsed-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                    <tr class="pc-grid-tr-first pc-grid-tr-last">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-30" align="center" valign="top" style="padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td class="pc-w620-padding-0-0-0-0" align="center" valign="top" style="padding: 0px 0px 0px 0px;">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-0-0-10-0" valign="top" style="padding: 0px 0px 8px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0" align="center">
                                  <div class="pc-font-alt pc-w620-fontSize-33px pc-w620-lineHeight-120pc" style="line-height: 120%; letter-spacing: -0px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 36px; font-weight: 600; font-variant-ligatures: normal; color: #ffffff; text-align: center; text-align-last: center;">
                                   <div><span>Exclusive Access</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-0-0-10-0" valign="top" style="padding: 0px 0px 8px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0" align="center">
                                  <div class="pc-font-alt pc-w620-fontSize-20px pc-w620-lineHeight-120pc" style="line-height: 120%; letter-spacing: -0px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 27px; font-weight: 300; font-variant-ligatures: normal; color: #ffffff; text-align: center; text-align-last: center;">
                                   <div><span style="font-weight: 300;font-style: normal;">Top Models Ready for Your Next Campaign</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-1-0-0-0" valign="top" style="padding: 0px 0px 32px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0" align="center">
                                  <div class="pc-font-alt pc-w620-fontSize-17px pc-w620-lineHeight-133pc" style="line-height: 160%; letter-spacing: -0px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 16px; font-weight: normal; font-variant-ligatures: normal; color: #ffffff; text-align: center; text-align-last: center;">
                                   <div><span>[NAME], we know the pressure of finding the right talent for your clients. That’s why we’ve made it easier than ever for you to access some of the most talented and versatile models who are ready to elevate your campaigns and exceed your expectations.</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td align="center" valign="top" style="padding: 0px 0px 40px 0px;">
                   <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                    <img src="https://cloudfilesdm.com/postcards/image-1726010611055.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0;" />
                   </a>
                  </td>
                 </tr>
                </table>
               </td>
              </tr>
             </table>
            </td>
           </tr>
          </table>
          <!-- END MODULE: Header -->
         </td>
        </tr>
        <tr>
         <td valign="top">
          <!-- BEGIN MODULE: Call to action -->
          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
           <tr>
            <td style="padding: 0px 0px 0px 0px;">
             <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
              <tr>
               <td valign="top" class="pc-w520-padding-30-40-30-40 pc-w620-padding-35-50-35-50" style="padding: 40px 60px 40px 60px; border-radius: 0px; background-color: #dad9d9;" bgcolor="#f3f3f3">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td align="center" valign="top" style="padding: 0px 0px 10px 0px;">
                   <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
                    <tr>
                     <td valign="top" align="center">
                      <div class="pc-font-alt" style="line-height: 128%; letter-spacing: -0.6px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 36px; font-weight: 800; font-variant-ligatures: normal; color: #151515; text-transform: uppercase; text-align: center; text-align-last: center;">
                       <div><span style="text-transform: uppercase;">Don’t miss this opportunity</span>
                       </div>
                      </div>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                   <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
                    <tr>
                     <td valign="top" align="center">
                      <div class="pc-font-alt" style="line-height: 140%; letter-spacing: -0.2px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 18px; font-weight: normal; font-variant-ligatures: normal; color: #1b1b1b; text-align: center; text-align-last: center;">
                       <div><span>Click the button below to schedule a call and secure your next models before they&#39;re gone!</span>
                       </div>
                      </div>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <th valign="top" align="center" style="padding: 0px 0px 20px 0px; text-align: center; font-weight: normal; line-height: 1;">
                   <!--[if mso]>
        <table border="0" cellpadding="0" cellspacing="0" role="presentation" align="center" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
            <tr>
                <td valign="middle" align="center" style="background-color: #ff0000; text-align:center; color: #ffffff; padding: 14px 18px 14px 18px; mso-padding-left-alt: 0; margin-left:18px;" bgcolor="#ff0000">
                                    <a class="pc-font-alt" style="display: inline-block; text-decoration: none; font-variant-ligatures: normal; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-weight: 500; font-size: 16px; line-height: 150%; letter-spacing: -0.2px; text-align: center; color: #ffffff;" href="mailto:schilling.caleb@yahoo.com" target="_blank"><span style="display: block;"><span style="font-family: 'Poppins', Arial, Helvetica, sans-serif;">CONTACT NOW</span></span></a>
                                </td>
            </tr>
        </table>
        <![endif]-->
                   <!--[if !mso]><!-- -->
                   <a style="display: inline-block; box-sizing: border-box; background-color: #ff0000; padding: 14px 18px 14px 18px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-weight: 500; font-size: 16px; line-height: 150%; letter-spacing: -0.2px; color: #ffffff; vertical-align: top; text-align: center; text-align-last: center; text-decoration: none; -webkit-text-size-adjust: none;" href="mailto:schilling.caleb@yahoo.com" target="_blank"><span style="display: block;"><span style="font-family: 'Poppins', Arial, Helvetica, sans-serif;">CONTACT NOW</span></span></a>
                   <!--<![endif]-->
                  </th>
                 </tr>
                </table>
               </td>
              </tr>
             </table>
            </td>
           </tr>
          </table>
          <!-- END MODULE: Call to action -->
         </td>
        </tr>
        <tr>
         <td valign="top">
          <!-- BEGIN MODULE: The Models -->
          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
           <tr>
            <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px;">
             <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
              <tr>
               <td valign="top" class="pc-w620-padding-20-24-32-24" style="padding: 36px 32px 56px 32px; border-radius: 0px; background-color: #020000;" bgcolor="#020000">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td class="pc-w620-spacing-0-0-24-0" align="center" valign="top" style="padding: 0px 0px 50px 0px;">
                   <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
                    <tr>
                     <td valign="top" class="pc-w620-padding-0-0-0-0" align="center">
                      <div class="pc-font-alt pc-w620-fontSize-25px" style="line-height: 160%; letter-spacing: 4px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 30px; font-weight: 800; font-variant-ligatures: normal; color: #ff0000; text-align: center; text-align-last: center;">
                       <div><span style="font-weight: 800;font-style: normal;color: rgb(255, 0, 0);">GET TO KNOW THE MODELS</span>
                       </div>
                      </div>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td class="pc-w620-spacing-0-0-32-0" style="padding: 0px 0px 0px 0px;">
                   <table class="pc-width-fill pc-w620-gridCollapsed-1" style="direction: rtl;" width="100%" dir="rtl" border="0" cellpadding="0" cellspacing="0" role="presentation">
                    <tr class="pc-grid-tr-first">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td class="pc-w620-halign-center pc-w620-valign-bottom" align="center" valign="middle">
                         <table class="pc-w620-halign-center" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td class="pc-w620-halign-center" align="center" valign="top">
                            <table class="pc-w620-halign-center" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-0-0-0-0" valign="top" style="padding: 0px 0px 20px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center" align="center">
                                  <div class="pc-font-alt pc-w620-textAlign-center" style="line-height: 160%; letter-spacing: 4px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 19px; font-weight: 600; font-variant-ligatures: normal; color: #ff0000; text-align: center; text-align-last: center;">
                                   <div><span style="color: rgb(255, 255, 255);">ALECIA LISAH</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726011462686.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0;" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726011567707.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr class="pc-grid-tr-last">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle" style="border: 1px solid transparent;">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726011760124.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td class="pc-w620-spacing-0-0-32-0" style="padding: 0px 0px 0px 0px;">
                   <table class="pc-width-fill pc-w620-gridCollapsed-1" style="direction: rtl;" width="100%" dir="rtl" border="0" cellpadding="0" cellspacing="0" role="presentation">
                    <tr class="pc-grid-tr-first">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-0-0-0-0" valign="top" style="padding: 0px 0px 20px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0" align="left">
                                  <div class="pc-font-alt" style="line-height: 160%; letter-spacing: 4px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 19px; font-weight: 600; font-variant-ligatures: normal; color: #ff0000; text-align: left; text-align-last: left;">
                                   <div><span style="color: rgb(255, 255, 255);">CALEB SCHILLING</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726014297450.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0;" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726014362663.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr class="pc-grid-tr-last">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle" style="border: 1px solid transparent;">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726014388899.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <td class="pc-w620-spacing-0-0-32-0" style="padding: 0px 0px 0px 0px;">
                   <table class="pc-width-fill pc-w620-gridCollapsed-1" style="direction: rtl;" width="100%" dir="rtl" border="0" cellpadding="0" cellspacing="0" role="presentation">
                    <tr class="pc-grid-tr-first">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td class="pc-w620-spacing-0-0-0-0" valign="top" style="padding: 0px 0px 20px 0px;">
                               <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0;">
                                <tr>
                                 <td valign="top" class="pc-w620-padding-0-0-0-0" align="left">
                                  <div class="pc-font-alt" style="line-height: 160%; letter-spacing: 4px; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 19px; font-weight: 600; font-variant-ligatures: normal; color: #ff0000; text-align: left; text-align-last: left;">
                                   <div><span style="color: rgb(255, 255, 255);">GIGI</span>
                                   </div>
                                  </div>
                                 </td>
                                </tr>
                               </table>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726016055567.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0;" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr>
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0; width: 100%;" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726016075654.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                    <tr class="pc-grid-tr-last">
                     <td class="pc-grid-td-first pc-grid-td-last pc-w620-itemsSpacings-0-32" align="center" valign="middle" style="width: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; direction: ltr;" dir="ltr">
                      <table style="border-collapse: separate; border-spacing: 0;" border="0" cellpadding="0" cellspacing="0" role="presentation">
                       <tr>
                        <td align="center" valign="middle" style="border: 1px solid transparent;">
                         <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                          <tr>
                           <td align="center" valign="top">
                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                             <tr>
                              <td align="center" valign="top" style="padding: 0px 0px 20px 0px;">
                               <a class="pc-font-alt" href="" target="_blank" style="text-decoration: none;">
                                <img src="https://cloudfilesdm.com/postcards/image-1726016101389.jpeg" class="" width="536" height="auto" alt="" style="display: block; outline: 0; line-height: 100%; -ms-interpolation-mode: bicubic; width:100%; height: auto; border: 0; box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);" />
                               </a>
                              </td>
                             </tr>
                            </table>
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                          <tr>
                           <td align="center" valign="top">
                           </td>
                          </tr>
                         </table>
                        </td>
                       </tr>
                      </table>
                     </td>
                    </tr>
                   </table>
                  </td>
                 </tr>
                </table>
               </td>
              </tr>
             </table>
            </td>
           </tr>
          </table>
          <!-- END MODULE: The Models -->
         </td>
        </tr>
        <tr>
         <td valign="top">
          <!-- BEGIN MODULE: Wide Button -->
          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
           <tr>
            <td style="padding: 0px 0px 0px 0px;">
             <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
              <tr>
               <td valign="top" class="pc-w520-padding-15-25-15-25 pc-w620-padding-15-30-15-30" style="padding: 15px 40px 100px 40px; border-radius: 0px; background-color: #060000;" bgcolor="#060000">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                 <tr>
                  <th valign="top" align="center" style="text-align: center; font-weight: normal; line-height: 1;">
                   <!--[if mso]>
        <table border="0" cellpadding="0" cellspacing="0" role="presentation" align="center" width="100%" style="border-collapse: separate; border-spacing: 0; margin-right: auto; margin-left: auto;">
            <tr>
                <td valign="middle" align="center" style="width: 100%; background-color: #ff0000; text-align:center; color: #ffffff; padding: 14px 18px 14px 18px; mso-padding-left-alt: 0; margin-left:18px;" bgcolor="#ff0000">
                                    <a class="pc-font-alt" style="display: inline-block; text-decoration: none; font-variant-ligatures: normal; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-weight: 500; font-size: 16px; line-height: 150%; letter-spacing: -0.2px; text-align: center; color: #ffffff;" href="mailto:schilling.caleb@yahoo.com" target="_blank"><span style="display: block;"><span style="color: rgb(255, 255, 255);">CONTACT NOW</span></span></a>
                                </td>
            </tr>
        </table>
        <![endif]-->
                   <!--[if !mso]><!-- -->
                   <a style="display: inline-block; box-sizing: border-box; background-color: #ff0000; padding: 14px 18px 14px 18px; width: 100%; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-weight: 500; font-size: 16px; line-height: 150%; letter-spacing: -0.2px; color: #ffffff; vertical-align: top; text-align: center; text-align-last: center; text-decoration: none; -webkit-text-size-adjust: none;" href="mailto:schilling.caleb@yahoo.com" target="_blank"><span style="display: block;"><span style="color: rgb(255, 255, 255);">CONTACT NOW</span></span></a>
                   <!--<![endif]-->
                  </th>
                 </tr>
                </table>
               </td>
              </tr>
             </table>
            </td>
           </tr>
          </table>
          <!-- END MODULE: Wide Button -->
         </td>
        </tr>
        
       </table>
      </td>
     </tr>
    </table>
   </td>
  </tr>
 </table>
 <!-- Fix for Gmail on iOS -->
 <div class="pc-gmail-fix" style="white-space: nowrap; font: 15px courier; line-height: 0;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
 </div>
</body>

</html>

"""
    return html_body