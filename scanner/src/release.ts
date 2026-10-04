export interface ReleaseMetrics{availability:number;coverage:number;recall20:number|null;recall50:number|null;recall100:number|null;falsePositiveRate:number|null}
export function canPromote(control:ReleaseMetrics,challenger:ReleaseMetrics,sample:number){
 if(sample<30)return {ok:false,reason:"insufficient_prospective_sample"};
 if(challenger.availability<.99||challenger.availability<control.availability)return {ok:false,reason:"availability_regression"};
 if(challenger.coverage<control.coverage)return {ok:false,reason:"coverage_regression"};
 if(control.falsePositiveRate!==null&&challenger.falsePositiveRate!==null&&challenger.falsePositiveRate>control.falsePositiveRate)return {ok:false,reason:"false_positive_regression"};
 const pairs:[number|null,number|null][]=[[control.recall20,challenger.recall20],[control.recall50,challenger.recall50],[control.recall100,challenger.recall100]];
 const improved=pairs.some(([a,b])=>a!==null&&b!==null&&b>a);
 if(!improved)return {ok:false,reason:"no_prospective_recall_improvement"};
 return {ok:true,reason:"promotion_gates_passed"}
}
