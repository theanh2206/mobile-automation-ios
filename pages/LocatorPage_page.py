from appium.webdriver.common.appiumby import AppiumBy



class LocatorPage:
    BUY_PAKAGE = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Mua gói"]')
    SEARCH_BOX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    SEARCH_BOX1 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm"]')
    SEARCH_BOX2 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm dịch vụ"]')
    SEARCH_DEALS = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm ưu đãi"]')
    SEARCH_INPUT = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm"]')
    AVATA = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
    MENU = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic leftBar blur"]')
    NOTIFICATION = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    DETAIL_D5 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvPackName" and @text="D5"]')
    REGISTER_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeButton')
    BUTTON_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCancelPackage")
    BUTTON_CONTINUTE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    BUTTON_CONTINUTE1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvContinue")
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
    INFORMATION = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Button"])[1]')
    INFOR_SUBCRIBER = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    INFOR_LOOKUP = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    BUTTON_BACK = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="arrow left roaming"]')
    BUTTON_BACK1 = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="icBack"]')
    BUTTON_UP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivUp")
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    BUTTON_BUY_PAKAGE = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]')
    BUTTON_REGISTER_KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvRegKNDL")
    KNDL = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
    # Hẹn roaming
    BUTTON_RESHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnDoiLichHen")
    BUTTON_CANCEL_SCHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnHuyRoaming")
    BUTTON_SUBMIT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnSubmit")
    ET_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etTime")
    BUTTON_SCHEDULE_ROAMING =(AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRoamingV2")
    #Liên hệ tư vấn
    BUTTON_CONTACT_CONSULTING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvContactConsultingV2")
    PHONE_NUMBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvPhoneNumber")
    DAY_CONTACT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/relaSelectDay")
    TIME_CONTACT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/relaShowSelectTime")
    SELECT_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvTime15To17")
    BOOK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSchedule")
    #Đổi số điện thoại con
    CHANGE_NUMBER = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/llChangeNumber"]/android.widget.ImageView')
    NEW_NUMBER = (AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlView"])[2]')
    ADD_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlAddPhone")
    INPUT_PHONE = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Số thuê bao"]')
    BUTTON_ACCEPT =(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Xác nhận"])[2]')
    # Banner
    BANNER = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER2 =(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER3 =(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER_KNDL = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER_SERVICES = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    #Tạo gói cước cá nhân
    PERSONAL_FLEX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    TIME_FLEX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    ICON_CVQT = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    BUTTON_CREATE_PAKAGE =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btCreatePackage")
    PAYMENT_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvPaymentConfirm")
    REGISTER_BUTTON2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btRegister")
    
    #Chuyển vùng quốc tế
    SEARCH_COUNTRY = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')
    SEARCH_BY_KEY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearchByKey")
    SEARCH_COUNTRY1 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm quốc gia"]')
    BUTTON_APPLY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvApply")
    CHECK_TRIP = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMsgPackageRoamFlexCreate")
    CREATE_PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCreatePackageRoamFlex")
    
    #Chọn chu kỳ gói cước
    RADIO_BUTTON_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbAll")
    RADIO_BUTTON_DAYS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbDays")
    RADIO_BUTTON_MONTHS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbMonths")
    
    #Bộ lọc theo giá, dung lượng
    SORT_PRICE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSortingPrice")
    SORT_DATA = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSortingData")
    
    #Màn tất cả gói cước
    VIEW_ALL_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llViewAll")
    BUTTON_DETAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvDetail")
    
    #Chia sẻ/tặng gói cước
    GIFT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivGift")
    PHONE_RECIEVE = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Nhập số điện thoại"]')
    GIFT_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btConfirm")
    ICON_SHARE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivShare")
    BUTTON_SHARE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvShare")
    
    #Mẹo tích điểm 
    SAVE_POINT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Mẹo tích điểm"]')
    
    #Lịch sử điểm
    POINT_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lịch sử đơn hàng"]')
    CART_HISTORY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvHistoryCart")
    CLOSE = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="add roam"]')
    BUTTON_CLOSE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btClose")
    BUTTON_CLOSE1 = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="close dt"]')
    #Đổi ưu đãi
    BUTTON_EXCHANGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvExchange")
    DEALS_LIST_ALL = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[1]')
    DEALS_LIST_ALL_OTHER = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[2]')
    
    #Kết nối dài lâu
    ADD_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btAdd")
    EXCHANGE_POINT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvExchanage")
    BUY_NOW = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyNow")
    KNDL_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnConfirm")
    BUTTON_SEE_MORE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlSeeMore")
    BUTTON_REFESH = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivUpdateRefresh")
    INPUT_MAIL = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Nhập email nhận ưu đãi"]')
    
    #Hồ sơ cá nhân
    BUTTON_DETAIL1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvDetails")
    BUTTON_DELETE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btDelete")
    SELECT_DATE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMonthYear")
    BUTTON_OK = (AppiumBy.ID, "android:id/button1")
    BUTTON_FILLTER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btFilter")
    ICON_BIN =(AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBin")
    BUTTON_UPDATE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btUpdate")
    SWITCH_LANGUAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/jtbSwitchLanguage")
    ON_SWITCH_NOTIFICATION = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="1"]')
    OFF_SWITCH_NOTIFICATION = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[1]')
    SMART_OTP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlSmartOtp")
    SWITCH_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="0"]')
    INPUT_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="Nhập mã PIN 4 chữ số"]')
    CONFIRM_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="Xác nhận mã PIN"]')
    ON_SWITCH_SPAM = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[1]')
    ON_SWITCH_BLOCK = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="0"]')
    OFF_SWITCH_SPAM = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[1]')
    OFF_SWITCH_BLOCK = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="1"]')
    