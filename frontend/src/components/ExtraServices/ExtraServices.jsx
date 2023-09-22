import { extraServices } from '../../utils/initialData'
import ExtraServiceField from '../ExtraServiceField/ExtraServiceField'
import './ExtraServices.scss'

function ExtraServices() {
  return (
    <div className="extra-service">
      <p className="text-l">Дополнительные услуги</p>
      <div className="extra-service__container">
        <div className="extra-service-fields__wrapper">
          {extraServices.map((extra, index) => (
            <ExtraServiceField
              key={extra.title}
              title={extra.title}
              price={extra.price}
              maxCount={extra.maxCount}
              index={index}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

export default ExtraServices