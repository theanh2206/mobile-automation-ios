from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage



class LocatorPage:
    BUY_PAKAGE = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[2]')
    SEARCH_BOX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch4x")
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    AVATA = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivAvatar")
    MENU = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivMenu")
    NOTIFICATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivNotification")
    DETAIL_D5 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvPackName" and @text="D5"]')
    REGISTER_BUTTON = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRegister")
    BUTTON_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCancelPackage")
    BUTTON_CONTINUTE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    BACKGROUND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBack")
    BUTTON_SEE_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSeeAll")
    RECHARGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRecharge")
    
    #---Dịch vụ mobigames
    MOBIGAMES_DETAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivThumb")
    MOBIGAMES_REGISTER1 = (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister"])[1]')
    MOBIGAMES_REGISTER2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    MOBIGAME_UNREGISTER = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister" and @text="Hủy"]')
    #---Gói cước của bạn
    BUTTON_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvExtendPackage")
    BUTTON_CANCEL_EXTEND = (AppiumBy.ID,"vms.com.vn.mymobifone:id/tvCancelExtendPackage")
    DETAIL_MY_PAKAGE = (AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlPB4"]')
    BUTTON_CONFIRM_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmExtend")
    BUTTON_CONFIRM_CANCEL_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmCancelExtend")
    #-- Thông tin sử dụng/tiện ích nổi bật
    CVQT = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[1]')
    KNDL1 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[4]')
    VTC83 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[5]')
    KHS = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[6]')
    BUTTON_BACK_LEFT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivLeftIcon")
    #--Tiện ích của bạn

    #--Tất cả tiện ích
    VIEW_ALL_UTILS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvViewAllUtils")
    BTN_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btCancel")
    INFORMATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llUsageInfos")
    INFOR_SUBCRIBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivArrowInfo")
    INFOR_LOOKUP = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineCheckCharges"]/android.widget.ImageView')
    BUTTON_BACK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBack")
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryTopup"]/android.widget.ImageView')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryPackage"]/android.widget.ImageView')
    BUTTON_BUY_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyPackage")
    BUTTON_REGISTER_KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvRegKNDL")
    KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivCardLoyalty")
    # Hẹn roaming
    BUTTON_RESHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnDoiLichHen")
    BUTTON_CANCEL_SCHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnHuyRoaming")
    BUTTON_SUBMIT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnSubmit")
    ET_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etTime")
    #Đổi số điện thoại con
    CHANGE_NUMBER = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/llChangeNumber"]/android.widget.ImageView')
    NEW_NUMBER = (AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlView"])[2]')
    ADD_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlAddPhone")
    INPUT_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPhoneNumber")
    BUTTON_ACCEPT =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btAccept")
    # Banner
    BANNER = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivBannerService"]')
    
    #Tạo gói cước cá nhân
    PERSONAL_FLEX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlPersonalFlex")
    TIME_FLEX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlTimeFlex")
    ICON_CVQT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlCvqt")
    BUTTON_CREATE_PAKAGE =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btCreatePackage")
    PAYMENT_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvPaymentConfirm")
    REGISTER_BUTTON2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btRegister")
    
    #Chuyển vùng quốc tế
    SEARCH_COUNTRY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSearchCountry")
    SEARCH_BY_KEY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearchByKey")
    SEARCH_COUNTRY1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch")
    BUTTON_APPLY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvApply")
    CHECK_TRIP = (AppiumBy.XPATH, '//android.widget.TextView[@text="Kiểm tra trước chuyến đi"]')
    PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMsgPackageRoamFlexCreate")
    CREATE_PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCreatePackageRoamFlex")