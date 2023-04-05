import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery

from keyboards import *
from config import TOKEN

API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Привет! Я бот, который позволит тебе узнать чуть больше обо мне",reply_markup=answer)


@dp.callback_query_handler(text='answer')
async def about(call: CallbackQuery):
    await call.message.answer(""""🙋‍♂️ Меня зовут Абдурахмон, я Junior-Python Программист , после окончания учебного курса ,  я работал над двумя проектами в общем счёте  4 месяцев. 

👨‍💻 Уже год как я изучаю и интересуюсь этим языком программирования. Здесь можете ознакомиться с моими проектами:

https://github.com/Abdurakhmon701""", reply_markup=cases)

@dp.callback_query_handler(text='cases')
async def about(call: CallbackQuery):
    await call.message.answer("""Я разработал 👨‍💻 Telegram бот для одного магазина, занимаюшаяся продажей 🪴 цветов и растений.
Пока-что считаю этот проект самым большим в моей карьере, так как в этом боте я сделал заказную корзину, а ещё привязал платёжную систему.
Этот бот был разработан с помощью Django, и соответственно имеет свой Back-End. В конце поста оставлю отдельные ссылки на самого бота и его бэкэнда.

Вот отрывок кода платежной системы:

------------------------------------------------------------------------------------
@dp.callback_query_handler(Text(startswith='payment_'),state=OrderInfoData.payment)
async def echo(call: types.CallbackQuery,state: FSMContext):
	all_data = call.data.index('_')
	pay = call.data[all_data+1:]
	await call.message.answer("<b> Минуточку.. </b>")
	information = get_basket_all_by_telegram_id(call.from_user.id)
	products_list = ''
	all_sum = 0
	if pay=="click":
		await state.update_data({"tulov":"click"})
		for info in  information:
			products_list+= f"\n{info['product_name']}\n"
			product_price = info['product_price']
			new_product_price = product_price.replace(' ',"")
			# print(f"{info['product_name']}*{info['count']}={int(new_product_price)*int(info['count'])},{info['product_price']}")
			all_sum += int(new_product_price)*int(info['count']) 

		product = Product(
			title="TestName",
			description="TestDescription",
			currency="UZS",
			prices=[
				LabeledPrice(
					label = f"{info['product_name']}",
					amount=all_sum*100,
					),
				LabeledPrice(
					label="Доставка",
					amount=5000000,
					),
				],
			start_parameter="create_invoice_python_book",
			provider_token = PROVIDER_TOKEN_CLICK
			)
		await bot.send_invoice(chat_id=call.from_user.id,**product.generate_invoice(),payload=f"{products_list}")
		await OrderInfoData.user_id.set()
--------------------------------------------------------------------------
Полный код самого бота: https://github.com/Abdurakhmon701/Flowers_Garden_Bot
Django: https://github.com/Abdurakhmon701/Flowers_Garden_Backend""", reply_markup=next)

@dp.callback_query_handler(text='next')
async def about(call: CallbackQuery):
    await call.message.answer("""Ещё один проект, которого я сделал - это InnoSchool. Здесь я разработал Backend и API, небольшой кейс.
Я разработал отдел новостей сайта, было забавно. Ознакомьтесь с Views файлом:

----------------------------------------------------------------------------
class NewsViewUzRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsUzSerializers(news)
		return Response(serializer.data)


class NewsViewRuRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsRuSerializers(news)
		return Response(serializer.data)


class NewsViewEnRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsEnSerializers(news)
		return Response(serializer.data)


class ListNewsUzAPI(ListAPIView):
	serializer_class = NewsUzSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination


class ListNewsRuAPI(ListAPIView):
	serializer_class = NewsRuSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination


class ListNewsEnAPI(ListAPIView):
	serializer_class = NewsEnSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination
----------------------------------------------------------------------------
Кейс: https://github.com/Abdurakhmon701/Inno-School""", reply_markup=contacts)

@dp.callback_query_handler(text='contacts')
async def about(call: CallbackQuery):
    await call.message.answer("Мой аккаунт: https://t.me/djuraev721")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)