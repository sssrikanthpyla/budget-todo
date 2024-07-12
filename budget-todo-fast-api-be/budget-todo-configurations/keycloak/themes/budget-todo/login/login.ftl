<#import "template.ftl" as layout>
    <@layout.registrationLayout displayInfo=social.displayInfo; section>
        <#if section="title">
            ${msg("loginTitle",(realm.displayName!''))}
            <#elseif section="header">
                <div class="title">
                    <span class="SafetyRiskAssessment">Sign In</span>   
                    <#-- ${msg("loginTitleHtml",(realm.displayNameHtml!''))?no_esc} -->
                </div>
                <#elseif section="form">
                    <#if realm.password>
                        <form id="kc-form-login" class="form ${properties.kcFormClass!}" action="${url.loginAction}" method="post">
                            <div class="username-container ${properties.kcFormGroupClass!}">
                                <div class="${properties.kcLabelWrapperClass!} label-contanier">
                                    <label for="username" class="${properties.kcLabelClass!}">
                                        <#if !realm.loginWithEmailAllowed>
                                            ${msg("username")}
                                            <#elseif !realm.registrationEmailAsUsername>
                                                ${msg("usernameOrEmail")}
                                                <#else>
                                                    ${msg("email")}
                                        </#if>
                                    </label>
                                </div>
                                <div class="${properties.kcInputWrapperClass!}">
                                    <#if usernameEditDisabled??>
                                        <input placeholder="username" id="username" class="form-control ${properties.kcInputClass!}" name="username" value="${(login.username!'')}" type="text" disabled />
                                        <#else>
                                            <input placeholder="username" id="username" class="form-control ${properties.kcInputClass!}" name="username" value="${(login.username!'')}" type="text" autofocus autocomplete="off" />
                                    </#if>
                                </div>
                            </div>
                            <div class="password-container ${properties.kcFormGroupClass!}">
                                <div class="${properties.kcLabelWrapperClass!} label-contanier">
                                    <label for="password" class="${properties.kcLabelClass!}">
                                        ${msg("password")}
                                    </label>
                                </div>
                                <div class="${properties.kcInputWrapperClass!}">
                                    <input placeholder="password" id="password" class="form-control ${properties.kcInputClass!}" name="password" type="password" autocomplete="off" />
                                </div>
                            </div>
                            <div class="${properties.kcFormGroupClass!} row third-container">
                                <div id="kc-form-options" class="${properties.kcFormOptionsClass!} checkbox-holder">
                                    <div class="col-xs-7">
                                        <#if realm.rememberMe && !usernameEditDisabled??>
                                            <div class="checkbox remember-me-checkbox">
                                                <label>
                                                    <#if login.rememberMe??>
                                                        <input id="rememberMe" name="rememberMe" type="checkbox" tabindex="3" checked>&nbsp;&nbsp;${msg("rememberMe")}
                                                        <#else>
                                                            <input id="rememberMe" name="rememberMe" type="checkbox" tabindex="3">&nbsp;&nbsp;${msg("rememberMe")}
                                                    </#if>
                                                </label>
                                            </div>
                                        </#if>
                                    </div>
                                    <div>
                                        <div class="${properties.kcFormOptionsWrapperClass!} col-xs-12 " id="kc-forgot">
                                            <#if realm.resetPasswordAllowed>
                                                <span><a href="${url.loginResetCredentialsUrl}">
                                                        ${msg("doForgotPassword")}
                                                    </a></span>
                                            </#if>
                                        </div>
                                    </div>
                                </div>
                                <div class="login-btn-holder">
                                    <div id="kc-form-buttons" class="col-xs-5 ${properties.kcFormButtonsClass!}">
                                        <div class="${properties.kcFormButtonsWrapperClass!}">
                                            <input class="login-btn btn btn-primary btn-flat btn-block ${properties.kcButtonClass!} ${properties.kcButtonPrimaryClass!} ${properties.kcButtonLargeClass!}" name="login" id="kc-login" type="submit" value="${msg("doLogIn")}" />
                                        </div>
                                        <div class="clearfix"></div>
                                    </div>
                                </div>
                                <#if (realm.password && realm.registrationAllowed && !usernameEditDisabled??) || realm.resetPasswordAllowed>
                                    <div class="register-btn-holder">
                                        <#if realm.password && realm.registrationAllowed && !usernameEditDisabled??>
                                            <div id="kc-registration" class="btn register-btn-login">
                                                <span>
                                                    <#-- ${msg("noAccount")} -->
                                                        <a href="${url.registrationUrl}">
                                                            ${msg("doRegister")}
                                                        </a>
                                                </span>
                                            </div>
                                        </#if>
                                    </div>
                                </#if>
                            </div>
                        </form>
                    </#if>
                    <#elseif section="info">
                        <#if realm.password && social.providers??>
                            <div id="kc-social-providers">
                                <ul>
                                    <#list social.providers as p>
                                        <li><a href="${p.loginUrl}" id="zocial-${p.alias}" class="zocial ${p.providerId}"> <span class="text">
                                                    ${p.displayName}
                                                </span></a></li>
                                    </#list>
                                </ul>
                            </div>
                        </#if>
        </#if>
    </@layout.registrationLayout>