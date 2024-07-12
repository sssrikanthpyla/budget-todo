<#macro registrationLayout bodyClass="" displayInfo=false displayMessage=true>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" class="${properties.kcHtmlClass!}">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="robots" content="noindex, nofollow">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <#if properties.meta?has_content>
            <#list properties.meta?split(' ') as meta>
            <meta name="${meta?split('==')[0]}" content="${meta?split('==')[1]}"/>
        </#list>
    </#if>
    <title><#nested "title"></title>
    <link rel="shortcut icon" href="${url.resourcesPath}/img/budget-todo.jpg" />
    <#if properties.styles?has_content>
        <#list properties.styles?split(' ') as style>
            <link href="${url.resourcesPath}/${style}" rel="stylesheet" />
        </#list>
    </#if>
    <#if properties.scripts?has_content>
        <#list properties.scripts?split(' ') as script>
            <script src="${url.resourcesPath}/${script}" type="text/javascript"></script>
        </#list>
    </#if>
    <#if scripts??>
        <#list scripts as script>
            <script src="${script}" type="text/javascript"></script>
        </#list>
    </#if>
</head>
<body class="${properties.kcBodyClass!} template">
<div class="main-container">
    <div class="login-img" >
    <img src="${url.resourcesPath}/img/budget-todo.jpg" alt="image of Shape"></img>
        <div class="image-content">
        <div class="image-title-1">Welcome to Budget Todo</div>
        <div class="image-border"></div>
        <div class="image-title-2">Budget Todo Application</div>
        <div class="image-title-3">""</div>
        </div>
    </div>
    <div id="kc-container" class="${properties.kcContainerClass!} form-container">
         <div class=budget-todo-logo>
       <img src="${url.resourcesPath}/img/budget-todo.jpg" alt="image of Shape"></img>
    </div>
        <div id="kc-container-wrapper" class="${properties.kcContainerWrapperClass!}">
            <div id="kc-content" class="${properties.kcContentClass!}">
             <div id="kc-header" class="${properties.kcHeaderClass!}">
                <div id="kc-header-wrapper" class="${properties.kcHeaderWrapperClass!}">
                <#--  <div><img id="logo" src="${url.resourcesPath}/img/armedulogo.png" alt="image of Shape" class="Shape"></img></div>  -->
        <div><span class="SafetyRiskAssessment">Sign In</span> <div class="sub-title">or use your user account</div> </div></div>
            </div>
                <div id="kc-content-wrapper" class="${properties.kcContentWrapperClass!}">
                    <#if displayMessage && message?has_content>
                        <div class="${properties.kcFeedbackAreaClass!}">
                            <div class="alert alert-${message.type}">
                                <#if message.type = ' success'><span class="${properties.kcFeedbackSuccessIcon!}"></span>
        </#if>
        <#if message.type='warning'><span class="${properties.kcFeedbackWarningIcon!}"></span></#if>
        <#if message.type='error'><span class="${properties.kcFeedbackErrorIcon!}"></span></#if>
        <#if message.type='info'><span class="${properties.kcFeedbackInfoIcon!}"></span></#if>
        <span class="kc-feedback-text">
            ${message.summary}
        </span>
        </div>
        </div>
        </#if>
        <div id="kc-form" class="${properties.kcFormAreaClass!}">
            <div id="kc-form-wrapper" class="${properties.kcFormAreaWrapperClass!}">
                <#nested "form">
            </div>
        </div>
        <#if displayInfo>
            <div id="kc-info" class="${properties.kcInfoAreaClass!}">
                <div id="kc-info-wrapper" class="${properties.kcInfoAreaWrapperClass!}">
                    <#nested "info">
                </div>
            </div>
        </#if>
        </div>
        </div>
        <#if realm.internationalizationEnabled>
            <div id="kc-locale" class="${properties.kcLocaleClass!}">
                <div id="kc-locale-wrapper" class="${properties.kcLocaleWrapperClass!}">
                    <div class="kc-dropdown language-picker" id="kc-locale-dropdown">
                        <div class="form-inline">
                            <div class="form-group">
                                <label for="language-picker-dropdown" class="language-picker-dropdown-label">
                                    <i class="fa fa-2x fa-globe"></i>
                                </label>
                                <select id="language-picker-dropdown" class="form-control" onchange="languageSelected()">
                                    <#list locale.supported as l>
                                        <#if l.label=locale.current>
                                            <option value="" selected>
                                                ${l.label}
                                            </option>
                                            <#else>
                                                <option value="${l.url}">
                                                    ${l.label}
                                                </option>
                                        </#if>
                                        <!-- <li class="kc-dropdown-item"><a href="${l.url}">
${l.label}
</a></li> -->
                                    </#list>
                                </select>
                                <!-- <a href="#" id="kc-current-locale-link">
${locale.current}
</a> -->
                            </div>
                            </form>
                        </div>
                    </div>
                </div>
        </#if>
        </div>
        </div>
        </div>
        </body>

    </html>
</#macro>